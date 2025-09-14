import tkinter as tk
from tkinter import ttk

def mostrar_resultado():
    # Opção única selecionada
    opcao = var_opcao.get()
    
    # Texto digitado
    texto = caixa_texto.get("1.0", tk.END).strip()
    
    # Caixa de marcar
    termo = "Sim" if var_termos.get() else "Não"
    
    # Exibe resultado
    resultado = f"Opção escolhida: {opcao}\n"
    resultado += f"Texto digitado: {texto}\n"
    resultado += f"Aceitou os termos? {termo}"
    lbl_resultado.config(text=resultado)

# Janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")
root.geometry("400x400")

# Caixa de seleção única (Radiobuttons)
ttk.Label(root, text="Escolha uma opção:").pack(anchor="w", padx=10, pady=(10,0))

opcoes = ["Python", "C", "Java", "JavaScript", "C++"]
var_opcao = tk.StringVar(value=opcoes[0])  # valor inicial

for opcao in opcoes:
    rb = ttk.Radiobutton(root, text=opcao, variable=var_opcao, value=opcao)
    rb.pack(anchor="w", padx=20)

# Caixa de texto
ttk.Label(root, text="Digite algo:").pack(anchor="w", padx=10, pady=(10,0))
caixa_texto = tk.Text(root, height=5, width=40)
caixa_texto.pack(padx=10, pady=5)

# Caixa de marcar
var_termos = tk.BooleanVar()
chk_termos = ttk.Checkbutton(root, text="Aceito os termos", variable=var_termos)
chk_termos.pack(anchor="w", padx=10, pady=5)

# Botão
btn = ttk.Button(root, text="Mostrar Resultado", command=mostrar_resultado)
btn.pack(pady=10)

# Label de saída
lbl_resultado = ttk.Label(root, text="", wraplength=350)
lbl_resultado.pack(pady=10)

root.mainloop()
