from tkinter import *
from tkinter import ttk
from usuarios.users_functions import *

def tela_login():
    #cria janela
    janela_login = Tk()
    #define título da janela
    janela_login.title("Tela de Login")
    #faz configurações da janela
    janela_login.configure(background="lightblue")
    #define tamanho inicial da janela
    janela_login.geometry("300x300")
    #define responsividade True = sim. (horizontal/x, vertical/y)
    janela_login.resizable(False, False)
    
    #FRAMES DA TELA
    
    #frame que mostra a operação de login
    frame_login = Frame(janela_login, bd= 4, bg= '#dfe3ee' ,highlightbackground= '#759fe6', highlightthickness=3)
    frame_login.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight=0.96)
    
    #Label informativa
    lb_info = Label(frame_login, text="Bem-vindo(a) ao sistema de gerenciamento\n de Papelaria!\nCadastre-se ou Efetue o Login.", bg= '#dfe3ee')
    lb_info.place(relx= 0.08, rely= 0.02)

    #label e entry Nome do usuário
    lb_username = Label(frame_login, text="Insira o Nome de Usuário", bg= '#dfe3ee')
    lb_username.place(relx= 0.22, rely= 0.23)

    entry_username = Entry(frame_login)
    entry_username.place(relx= 0.22, rely= 0.3, relwidth=0.55, relheight=0.08)

    #label e entry Senha
    lb_password = Label(frame_login, text="Insira a Senha", bg= '#dfe3ee')
    lb_password.place(relx= 0.22, rely= 0.43)

    entry_password = Entry(frame_login)
    entry_password.place(relx= 0.22, rely= 0.5, relwidth=0.55, relheight=0.08)

    #botões FRAME Options 
    bt_submit = Button(frame_login, text="Autenticar", bd=3, command=login)
    bt_submit.place(relx= 0.22, rely= 0.63, relwidth= 0.23, relheight= 0.08)

    bt_register = Button(frame_login, text="Registrar", bd=3, command=insert_user)
    bt_register.place(relx= 0.55, rely= 0.63, relwidth= 0.23, relheight= 0.08)
    #executa a tela e mantém rodando
    janela_login.mainloop()    