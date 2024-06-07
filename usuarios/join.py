import sqlite3

conexao = sqlite3.connect('papelaria_db.sqlite')
cursor = conexao.cursor()
    
def select_com_join():
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()   
    all_users = cursor.execute("""
        SELECT username, prod_name FROM users JOIN products
    """).fetchall()
    print(all_users)
    conexao.close()  
    
select_com_join()