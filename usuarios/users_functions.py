import sqlite3
import bcrypt
user = ''

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()

#CREATE USER
def insert_user(username, password):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    new_password = criptografar(password)
    cursor.execute("""
        INSERT INTO users(username, password) VALUES (?, ?)
    """, [username, new_password])
    conexao.commit()
    conexao.close()

#READ USER
def list_user():
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    all_users = cursor.execute("""
        SELECT user_ID, username FROM users
    """).fetchall()
    print(all_users)
    conexao.close()

#READ user_ID BY username
def get_user_id(username):
    search_term = f'%{username}%'
    cursor.execute("SELECT user_id FROM users WHERE username = ?", (search_term,))
    user = cursor.fetchone()    
    if user:
        return user[0]
    else:
        return None

#READ USER BY ID
def list_user_ByID(user_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    users_ByID= cursor.execute("""
        SELECT user_ID, username FROM users WHERE user_ID = ?
    """, [user_ID]).fetchone()
    print(users_ByID)
    conexao.close()    

#UPDATE PASSWORD BY ID
def update_password(password, user_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    sql = "UPDATE users SET password = ? WHERE user_ID = ?"
    cursor.execute( sql , (password, user_ID, ))
    conexao.commit()
    conexao.close()

#DELETE USER
def remove_user (user_ID):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    sql = "DELETE FROM users WHERE user_ID=?"
    cursor.execute( sql , (user_ID, ))
    conexao.commit()
    conexao.close()
    list_user()
    
#FUNÇÃO RESPONSÁVEL PELO LOGIN
def login(username, password):
    conexao = sqlite3.connect('papelaria_db.sqlite')
    cursor = conexao.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    user = cursor.execute(sql, [username]).fetchone()
    conexao.close()
    return user and checar_password(password, user[2])

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