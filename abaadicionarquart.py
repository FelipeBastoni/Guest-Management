import tkinter as tk
import shelve
from Obj import *
from datetime import datetime




def abaadicionarquart(main, menu, quartos, guardconteudo):


    #aba do gerenciamento

    def gerenc():

        fech()

        txtcadast.place(x=10,y=50)
        txtnm.place(x=10, y=100)
        entrcadast.place(x=10, y=150)
        txtpr.place(x=10, y=200)
        entrcadast2.place(x=10, y=250)
        btncadast.place(x=10, y=300)




    ##criador de quartos

    def nvquarto():

        cd = [ (entrcadast.get(), entrcadast2.get(), "Disponível", "") ]

        for nome, preco, dispn, ocpant in cd:

            quarto = Quarto(nome, preco, dispn, ocpant)
            quartos.append(quarto)

        with shelve.open("quartos.db") as db:

            for i in range(1):

                i = len(db)
                db[f"{i}"] = quarto

                conteudo = db[f"{i}"]
                guardconteudo.append(conteudo)












    #adicionarquarto

    botaogeren = tk.Button(menu, width= 15, text="Adicionar Quarto", command= gerenc)
    botaogeren.place(x=10, y=210)

    txtcadast = tk.Label(main, text="Cadastro de quarto: ", font=("Arial", 16))
    txtnm = tk.Label(main, text="Nome do Quarto:", font=("Arial", 16))
    entrcadast = tk.Entry(main, width= 50)
    txtpr = tk.Label(main, text="Preço do Quarto:", font=("Arial", 16))
    entrcadast2 = tk.Entry(main, width= 20)
    btncadast = tk.Button(main, text="cadastre", font=("arial",16), command= nvquarto)



    #função fechar
    def fech():

        txtcadast.place_forget()
        entrcadast.place_forget()
        entrcadast2.place_forget()
        btncadast.place_forget()
        txtnm.place_forget()
        txtpr.place_forget()

