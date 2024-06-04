import sqlite3
import bcrypt
user = ''

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()

#CREATE USER
def insert_user(username, password):
    new_password = criptografar(password)
    cursor.execute("""
        INSERT INTO users(username, password) VALUES (?, ?)
    """, [username, new_password])
    conexao.commit()

#UTILIZAR PARA ALIMENTAR A FUNÇÃO E CHAMAR NO ARQUIVO MAIN

#new_email = str(input("Digite seu email: "))
#new_password = str(input("Digite sua senha: "))
#insert_user(new_email, new_password)

#READ USER
def list_user():
    all_users = cursor.execute("""
        SELECT user_ID, username FROM users
    """).fetchall()
    print(all_users)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR USUÁRIOS
#list_user()

#READ USER BY ID
def list_user_ByID(user_ID):
    users_ByID= cursor.execute("""
        SELECT user_ID, username FROM users WHERE user_ID = ?
    """, [user_ID]).fetchone()
    print(users_ByID)

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE LISTAR USUÁRIOS

#new_ID = int(input("Digite o ID do usuário: "))
#list_user_ByID(new_ID)

#FUNÇÃO RESPONSÁVEL PELO LOGIN
def login(username, password):
    sql = "SELECT * FROM users WHERE username = ?"
    user = cursor.execute(sql, [username]).fetchone()
    
    return user and checar_password(password, user[2])

#UPDATE USERNAME BY ID (REFORMULAR IDEIA)
def update_username_byID(user_ID):
    print("\n---Autenticação---")
    aut_username = str(input("Digite seu username: "))  
    aut_password = str(input("Digite sua senha: "))  
    autenticado = login(aut_username, aut_password)
    if autenticado:
        new_username = str("Digite o novo username: ")
        cursor.execute("""
            UPDATE users SET username = ? WHERE user_ID = ?
        """, [new_username, user_ID])
        print("Alteração realizada com sucesso.")
    else: 
        print("Acesso Negado.")

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE ATUALIZAR USERNAME PELO ID
#new_ID = int(input("Digite o ID do usuário que deseja alterar: "))  
#update_username_byID(new_ID)

#UPDATE PASSWORD BY ID
def update_password(password, user_ID):
    sql = "UPDATE users SET password = ? WHERE user_ID = ?"
    cursor.execute( sql , (password, user_ID, ))
    conexao.commit()

#UTILIZAR QUANDO FOR CHAMAR A FUNÇÃO DE ATUALIZAR PRODUTOS PELO ID
#new_ID = int(input("Digite o ID do produto que deseja alterar: ")) 
#new_name = str(input("Digite o novo nome do produto: "))  
#new_price = int(input("Digite o novo preço do produto: "))  
#update_product(new_name, new_price, new_ID)

def remove_user (user_ID):
    sql = "DELETE FROM users WHERE user_ID=?"
    cursor.execute( sql , (user_ID, ))
    conexao.commit()
    list_user()

def criptografar(password):
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed

def checar_password(password, hashed):
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)

def get_auth_user():
    return user

def set_user_logged_in(cursor, username):
    global user
    # Obtém o usuário pelo nome de usuário fornecido
    cursor.execute("""
        SELECT * FROM users WHERE username = ?
    """, (username,))
    user = cursor.fetchone()

def get_user_id(username):
    cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        return None