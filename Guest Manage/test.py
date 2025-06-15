import tkinter as tk


def tela(janela):

    menu = tk.Frame(janela, width=250, bg="lightblue")
    menu.pack(side=tk.LEFT, fill=tk.Y)

    main = tk.Frame(janela, width=700, bg="red")
    main.pack(side=tk.RIGHT, fill="both", expand="true")