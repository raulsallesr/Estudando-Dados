import tkinter as tk

# Janela principal
janela = tk.Tk() # cria a janela principal
janela.title("Agenda de Contatos")
janela.geometry("700x550")

# Nome e Número
# label = etiqueta
tk.Label(janela, text="Nome: ").pack(pady=5) # pady é o espaço vertical # janela é onde vai aparecer e o .pack diz que vamos colocar na tela
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Número: ").pack(pady=5) # pady é o espaço vertical # janela é onde vai aparecer e o .pack diz que vamos colocar na tela
entrada_numero = tk.Entry(janela, width=40)
entrada_numero.pack()

# Botões
tk.Button(janela, text="Adicionar Contato", command=lambda: print("Isso ai")).pack(pady=10)
tk.Button(janela, text="Remover Contato", command=lambda: print("Isso ai")).pack(pady=10)
tk.Button(janela, text="Lista de Contatos", command=lambda: print("Isso ai")).pack(pady=10)
tk.Button(janela, text="Sair", command=lambda: print("Isso ai")).pack(pady=10)

# Lista de Contato
tk.Label(janela, text="Lista de Contatos: ").pack(pady=10)
lista_contatos = tk.Listbox(janela, width=40, height= 8)
lista_contatos.pack()

janela.mainloop() # isso que chama a janela
