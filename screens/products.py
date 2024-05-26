from tkinter import *
from tkinter import ttk
from screens.buttons import *

def tela_produtos():
    
    #cria janela
    janela_produtos = Tk()
    
    #define título da janela
    janela_produtos.title("Tela Produtos")
    
    #faz configurações da janela
    janela_produtos.configure(background="lightblue")
    
    #define tamanho inicial da janela
    janela_produtos.geometry("600x600")
    
    #define responsividade True = sim. (horizontal/x, vertical/y)
    janela_produtos.resizable(False, False)
    
    #define tamanho máximo
    janela_produtos.maxsize(width=900, height=700)
    
    #define tamanho mínimo
    janela_produtos.minsize(width=500, height=400)
    
    #frames da tela
    
    #frame que mostra opções
    frame_options = Frame(janela_produtos, bd= 4, bg= '#dfe3ee' ,highlightbackground= '#759fe6', highlightthickness=3)
    frame_options.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight=0.46)
    
    #frame que mostra saídas
    frame_show = Frame(janela_produtos, bd= 4, bg= '#dfe3ee' ,highlightbackground= '#759fe6', highlightthickness=3)
    frame_show.place(relx= 0.02, rely=0.5, relwidth= 0.96, relheight=0.46)
    
    #botões FRAME Options CRUD
    bt_limpar = Button(frame_options, text="Limpar", bd=3)
    bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.1)

    bt_buscar = Button(frame_options, text="Buscar", bd=3)
    bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.1)

    bt_limpar = Button(frame_options, text="Novo", bd=3)
    bt_limpar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.1)

    bt_alterar = Button(frame_options, text="Alterar", bd=3)
    bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.1)

    bt_apagar = Button(frame_options, text="Apagar", bd=3)
    bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.1)

    #label e entry do código
    lb_codigo = Label(frame_options, text="Código", bg= '#dfe3ee')
    lb_codigo.place(relx=0.05 , rely= 0.02)

    entry_codigo = Entry(frame_options)
    entry_codigo.place(relx=0.05 , rely= 0.1, relwidth=0.08, relheight=0.1)

    #label e entry Nome do usuário
    lb_username = Label(frame_options, text="Insira o Nome de Usuário", bg= '#dfe3ee')
    lb_username.place(relx=0.05 , rely= 0.35)

    entry_username = Entry(frame_options)
    entry_username.place(relx=0.05 , rely= 0.45, relwidth=0.35, relheight=0.1)

    #label e entry Senha
    lb_password = Label(frame_options, text="Insira a Senha", bg= '#dfe3ee')
    lb_password.place(relx=0.05 , rely= 0.58)

    entry_password = Entry(frame_options,)
    entry_password.place(relx=0.05 , rely= 0.68, relwidth=0.35, relheight=0.1)

    #treeview do frame show
    listaCli = ttk.Treeview(frame_show, height= 3, columns=("col1", "col2", "col3", "col4"))
    #enuncia os cabeçalhos
    listaCli.heading("#0", text="")
    listaCli.heading("#1", text="ID")
    listaCli.heading("#2", text="Nome")
    listaCli.heading("#3", text="Telefone")
    listaCli.heading("#4", text="Codigo")
    #define tamanhos
    listaCli.column("#0", width=1)
    listaCli.column("#1", width=50)
    listaCli.column("#2", width=200)
    listaCli.column("#3", width=125)
    listaCli.column("#4", width=125)
    #place
    listaCli.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)
    #barra de rolagem
    scroll_lista = Scrollbar(frame_show, orient='vertical')
    listaCli.configure(yscroll = scroll_lista.set)
    #posiciona e define o tamanho
    scroll_lista.place(relx=0.96 ,rely= 0.01, relwidth=0.04, relheight= 0.85)

   
    
    #executa a janela e mantém rodando
    janela_produtos.mainloop()


