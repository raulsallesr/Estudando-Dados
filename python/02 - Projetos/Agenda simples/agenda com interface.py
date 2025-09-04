import tkinter as tk

janela = tk.Tk() # cria a janela principal

janela.title("Oi")
janela.geometry("700x550")

tk.Label(janela, text="Olá! ").pack()
# label = etiqueta
# janela é onde vai aparecer e o .pack diz que vamos colocar na tela

tk.Button(janela, text="Botão", command=lambda: print("Isso ai")).pack()
tk.Message(janela, text="Oiee").pack()

janela.mainloop() # isso que chama a janela
