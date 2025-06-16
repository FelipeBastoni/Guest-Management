import tkinter as tk
import shelve 
from datetime import datetime
from Obj import *




def abaregistroclientes(menu, grap, main, a, janela):

    def regs():

        reg.place(x=10, y=50)

        with shelve.open("data/registro.db") as db:

            for a in range(len(db)):

                hist = tk.Label(janela, font=("Arial", 16), text=f"{db[f"{a}"]}", justify="left")
                hist.place(x=350, y=60*(a+2))
                grap.append(hist)



    botaoreg = tk.Button(menu, width= 15, text="Registro de Clientes", command= regs)
    botaoreg.place(x=10, y=130)

    reg = tk.Label(main, font=("Arial", 16), text="Registro de Estadias:")


