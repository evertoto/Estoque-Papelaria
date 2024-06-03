import sqlite3
from usuarios.users_functions import *
from produtos.product_functions import *
from data.settings import *

#estabelece a conexão com o banco de dados
conexao = sqlite3.connect('papelaria_db.sqlite')
#cria o cursor, o intermédio entre o código e o banco de dados
cursor = conexao.cursor()

create_table_prod()
create_table_user()
create_table_prod_user()

def get_user_id(username):
    cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        return None

username = str(input("Digite o username: "))
password = str(input("Digite a senha: "))
user_id = get_user_id(username)
autenticado = login(username, password)
set_user_logged_in(cursor, username)
if autenticado:
    print("Usuário autenticado")
else:
    print("Usuário ou senha incorreto(s), por favor tente novamente.")
#fazer o menu com todas as opções
while(True):
    print("""
        1- Cadastrar Usuario
        2- Realizar o login 
          --- ABA DOS USUÁRIOS ---
        3- Mostrar todos os Usuários
        4- Mostrar Usuário por ID 
        5- Atualizar Password
        6- Excluir Usuário
          --- ABA DOS PRODUTOS ---
        7- Cadastrar Produto
        8- Mostrar todos os Produtos
        9- Mostrar Produto por ID
        10- Atualizar Produto por ID
        11- Excluir Produto
          
        0- Encerrar programa
          
    """)
    opc = int(input("Digite a opção: "))
    
    if opc == 1:
        username = str(input("Digite o username: "))
        password = str(input("Digite a senha: "))
        insert_user(username, password)

    elif opc == 3:
        list_user()

    elif opc == 4:
        new_ID = int(input("Digite o ID do usuário que quer visualizar: "))
        list_user_ByID(new_ID)
    
    elif opc == 5:
        user_ID = int(input("Qual é o seu ID?  "))
        password = str(input("Qual será a nova senha?  "))
        update_password(password, user_ID)
        print("Senha atualizada com sucesso")

    elif opc == 6:
        list_user()
        user_id = int(input("Qual o ID do usuario que deseja excluir? "))
        remove_user(user_id) 

    elif opc == 7:
        new_product = str(input("Digite o nome do produto: "))
        new_price = float(input("Digite o preço do produto: "))
        productID =  insert_product(new_product, new_price)
        user = get_auth_user()
        print(user)
        insert_product_for_user(user[0], productID)
       
    elif opc == 8:
        list_products()
    
    elif opc == 9:
        new_ID = int(input("Digite o ID do produto que quer visualizar: "))
        list_products_ByID(new_ID)

    elif opc == 10:
        list_products()
        new_ID = int(input("Digite o ID do produto que deseja alterar: ")) 
        new_name = str(input("Digite o novo nome do produto: "))  
        new_price = int(input("Digite o novo preço do produto: "))  
        update_product_ByID(new_name, new_price, new_ID)

    elif opc == 11:
        list_products()
        prod_id = int(input("Qual o id do produto no qual deseja a exclusão:"))
        remove_product(prod_id)

    elif opc == 0:
        break
    else:
        print("Entrada Inválida. Tente novamente.")