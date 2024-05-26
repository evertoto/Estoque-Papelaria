from tkinter import *
from tkinter import ttk
from screens.products import *

def limpa_tela(entry_codigo, entry_username, entry_password):
    entry_codigo.delete(0, END)
    entry_username.delete(0, END)
    entry_password.delete(0, END)
    