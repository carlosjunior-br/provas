"""
[PY-A10] Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter
em Python. O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver
o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.
"""
import tkinter as tk
from tkinter import messagebox

def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    root.geometry(f"{largura}x{altura}+{x}+{y}")

def enviar():
    email_correto = False
    senha_correta = False
    if "@" in entry_email.get():
        email_correto = True
    if len(entry_senha.get()) > 6:
        senha_correta = True
    if not email_correto and not senha_correta:
        messagebox.showinfo("Aviso", f" Verifique seu e-mail! Ele deve conter '@'.\n Verifique senha senha! Ela deve ter mais de 6 dígitos.")
        entry_email.focus()
    elif not email_correto:
        messagebox.showinfo("Aviso", "Verifique seu e-mail! Ele deve conter '@'.")
        entry_email.focus()
    elif not senha_correta:
        messagebox.showinfo("Aviso", "Verifique senha senha! Ela deve ter mais de 6 dígitos.")
        entry_senha.delete(0, tk.END)
        entry_senha.focus()
    else:
        messagebox.showinfo("Aviso", "Login realizado com sucesso!")
        janela.destroy()

janela = tk.Tk()
janela.title("Interface de login")

largura_janela = 400
altura_janela = 160
centralizar_janela(janela, largura_janela, altura_janela)

fonte = ("Arial", 14)
fonte_menor = ("Arial", 10)

label_email = tk.Label(janela, text="Digite seu e-mail: ", font=fonte)
entry_email = tk.Entry(janela, font=fonte)
label_senha = tk.Label(janela, text="Digite sua senha: ", font=fonte)
entry_senha = tk.Entry(janela, font=fonte, show='*')
label_padrao = tk.Label(janela, text="A senha deve ter mais de 6 dígitos", font=fonte_menor)
botao_enviar = tk.Button(janela, text="Fazer login", font=fonte, width=20, command=enviar)

label_email.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_email.grid(row=0, column=1, padx=5, pady=5, sticky="w")
label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_senha.grid(row=1, column=1, padx=5, pady=5, sticky="w")
label_padrao.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
botao_enviar.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

entry_email.focus()

janela.mainloop()