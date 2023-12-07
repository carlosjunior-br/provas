"""
[PY-A09]Desenvolva uma calculadora simples utilizando a biblioteca Tkinter em Python.
A calculadora deve permitir a realização das operações básicas (adição, subtração, multiplicação e divisão) e ser
capaz de lidar com entradas de números inteiros e decimais.
Além disso, a interface da calculadora deve ser intuitiva e fácil de usar para o usuário.
"""
import tkinter as tk
from tkinter import messagebox

def centralizar_janela(root, largura, altura):
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    root.geometry(f"{largura}x{altura}+{x}+{y}")

def inserir_valor(campo, valor):
    conteudo_atual = campo.get()
    novo_conteudo = conteudo_atual + valor
    campo.set(novo_conteudo)

def resultado(campo):
    conteudo_atual = campo.get()
    try:
        resultado = eval(conteudo_atual)
        campo.set(resultado)
    except Exception:
        messagebox.showinfo("Erro", "Expressão inválida!")
        campo.set("")

def limpar(campo):
    campo.set("")

def fechar_janela():
    janela.destroy()

janela = tk.Tk()
janela.title("Calculadora")

largura_janela = 450
altura_janela = 450

centralizar_janela(janela, largura_janela, altura_janela)

fonte = ("Arial", 20)
fonte_botao = ("Arial", 20)



titulo = tk.Label(janela, text="Calculadora", font=fonte)
valor = tk.StringVar(janela)
label_valor = tk.Label(janela, textvariable=valor, font=fonte, background="#FFFFFF", width=25)
numeros = tk.Frame(janela)
botao_9 = tk.Button(numeros, text="9", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "9"))
botao_8 = tk.Button(numeros, text="8", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "8"))
botao_7 = tk.Button(numeros, text="7", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "7"))
botao_6 = tk.Button(numeros, text="6", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "6"))
botao_5 = tk.Button(numeros, text="5", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "5"))
botao_4 = tk.Button(numeros, text="4", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "4"))
botao_3 = tk.Button(numeros, text="3", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "3"))
botao_2 = tk.Button(numeros, text="2", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "2"))
botao_1 = tk.Button(numeros, text="1", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "1"))
botao_0 = tk.Button(numeros, text="0", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "0"))
botao_ponto = tk.Button(numeros, text=".", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "."))
botao_igual = tk.Button(numeros, text="=", font=fonte_botao, width=5, command=lambda: resultado(valor))
botao_divisao = tk.Button(numeros, text="/", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "/"))
botao_multiplicacao = tk.Button(numeros, text="X", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "*"))
botao_subtracao = tk.Button(numeros, text="-", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "-"))
botao_adicao = tk.Button(numeros, text="+", font=fonte_botao, width=5, command=lambda: inserir_valor(valor, "+"))
inferior = tk.Frame(janela)
botao_limpar = tk.Button(inferior, text="Limpar", font=fonte_botao, width=8, command=lambda: limpar(valor))
botao_fechar = tk.Button(inferior, text="Sair", font=fonte_botao, width=8, command=fechar_janela)

titulo.pack(padx=10, pady=5)
label_valor.pack(padx=10, pady=5)

numeros.pack()
inferior.pack()

botao_9.grid(row=0, column=2, padx=10, pady=5, sticky="ew")
botao_8.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
botao_7.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
botao_6.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
botao_5.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
botao_4.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
botao_3.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
botao_2.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
botao_1.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
botao_igual.grid(row=3, column=2, padx=10, pady=5, sticky="ew")
botao_0.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
botao_ponto.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
botao_divisao.grid(row=0, column=3, padx=10, pady=5, sticky="ew")
botao_multiplicacao.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
botao_subtracao.grid(row=2, column=3, padx=10, pady=5, sticky="ew")
botao_adicao.grid(row=3, column=3, padx=10, pady=5, sticky="ew")
botao_limpar.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
botao_fechar.grid(row=4, column=3, padx=10, pady=5, sticky="ew")

janela.mainloop()