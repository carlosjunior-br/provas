"""
[PY-A09] Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de
centímetros para metros.
"""
import tkinter as tk

def converter():
    try:
        unidade_cm = float(entry_unidade_cm.get())
        unidade_m = unidade_cm / 100
        unidade_m_texto.set(f"{unidade_cm:.2f} cm é igual a {unidade_m:.2f} metros.")
        entry_unidade_cm.delete(0, tk.END)

    except ValueError:
        unidade_m_texto.set("Insira um valor válido.")

janela = tk.Tk()
janela.title("Conversor de centímetros para metros")

fonte = ("Arial", 16)
unidade_m_texto = tk.StringVar()
unidade_m_texto.set("")

label_unidade = tk.Label(janela, text="Unidade de medida em centímetros (cm):", font=fonte)
entry_unidade_cm = tk.Entry(janela, font=fonte)
botao_converter = tk.Button(janela, text="Converter para metros", font=fonte, width=20, command=converter)
label_unidade_m = tk.Label(janela, textvariable=unidade_m_texto, font=fonte)

label_unidade.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_unidade_cm.grid(row=0, column=1, padx=10, pady=5)
botao_converter.grid(row=1, column=0, columnspan=2, pady=10)
label_unidade_m.grid(row=2, column=0, columnspan=2, pady=5)
entry_unidade_cm.focus()

janela.mainloop()