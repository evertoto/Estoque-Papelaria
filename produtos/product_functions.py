import sqlite3
conexao = sqlite3.connect('papelaria_db.sqlite')
cursor = conexao.cursor()

#CREATE PRODUCT
def insert_product(name, price):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO products(prod_name, prod_price) VALUES (?, ?)
    """, [name, price])
    conexao.commit()
    conexao.close()
    return cursor.lastrowid  # Return the ID of the last inserted row

#READ PRODUCT
def list_products():
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    all_products = cursor.execute("""
        SELECT * FROM products
    """).fetchall()
    print(all_products)
    conexao.close()


#READ USER BY ID
def list_products_ByID(prod_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    products_ByID= cursor.execute("""
        SELECT * FROM products WHERE prod_ID = ?
    """, [prod_ID]).fetchone()
    print(products_ByID)
    conexao.close()

#READ PRODUCT BY NAME
def list_product_by_name(prod_name):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    search_product = f"%{prod_name}%"
    products_ByName= cursor.execute("""
        SELECT * FROM products WHERE prod_name LIKE ?
    """, [search_product]).fetchall()
    print(products_ByName)
    conexao.close()

#UPDATE PRODUCTS BY ID
def update_product_ByID(prod_name, prod_price, prod_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    new_product = cursor.execute("""
        UPDATE products SET prod_name = ?, prod_price = ? WHERE prod_ID = ?
    """, [prod_name, prod_price, prod_ID])
    conexao.commit()
    list_products()
    conexao.close()

#DELETE PRODUCT BY ID
def remove_product (prod_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    sql = "DELETE FROM products WHERE prod_ID=?"
    cursor.execute( sql , (prod_ID, ))
    conexao.commit()
    list_products()
    conexao.close()

#CREATE NEW PRODUCT (tabela conjugada)
def insert_product_for_user(user_ID, prod_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO user_product (user_ID, prod_ID)
        VALUES (?, ?)
    """, (user_ID, prod_ID))
    conexao.commit()
    conexao.close()
