import tkinter as tk
from tkinter import ttk


def limpar():
    entry.delete(0, tk.END)
    resultado_var.set("") 
    
def calcular():
    expressao = entry.get()
    try:
        # Avalia a expressão (ex: "12+7", "3*5", "10-2")
        resultado = eval(expressao)
        entry.delete(0, tk.END)  # Limpa a entrada após calcular
        entry.insert(tk.END, str(resultado))  # Insere o resultado na entrada
        resultado_var.set("")  

       # entry = tk.Entry(janela, textvariable=resultado_var, font=("Arial", 12, "bold"))
    except Exception:
        entry.delete(0, tk.END)  # Limpa a entrada após calcular
        resultado_var.set("Erro: Expressão inválida!") 
        entry.insert(tk.END, resultado_var.get())  # Insere o resultado na entrada

def botao_teclado(tecla):
    if tecla == "C" or tecla == "Limpar":
        limpar()
    elif tecla == "Sair":
        janela.quit()
    elif tecla == "=":
        calcular()
    else:
        entry.insert(tk.END, tecla)

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x300")

# Variável global para armazenar resultado
resultado_var = tk.StringVar()

# Entrada única para a expressão completa
entry = tk.Entry(janela, font=("Arial", 16))
entry.pack(pady=10, padx=10, fill=tk.X)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

numeros = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),       
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), 
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), 
    ('+', 4, 0), ('-', 4, 1), ('*', 4, 2),
    ('C', 5, 0), ('Limpar', 5, 1), ('Sair', 5, 2)
]

for texto, linha, coluna in numeros:
    tk.Button(frame_botoes, text=texto, width=5, command=lambda t=texto: botao_teclado(t)).grid(row=linha, column=coluna, padx=5, pady=5)

janela.mainloop()
