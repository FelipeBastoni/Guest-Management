import tkinter as tk
import shelve 
from datetime import datetime







def atualizar_hora(HRA):

    HRA.clear()

    data_hora_atua = datetime.now()
    data_formatad = data_hora_atua.strftime("%d-%m-%Y - %H:%M:%S") 
    #janela.after(60000, atualizar_hora) #valor em mseg

    print(data_formatad)
    HRA.append(data_formatad)




# #função fechar
# def fech():

#     lamp()
#     limp()  
#     txtqts.place_forget()



#lista de quartos da hospedagem


def abaquartos(janela, menu, main, guardconteudo, grapc, grap):

    def quats(): 



        # fech()
        txtqts.place(x=10, y=50)

        for y in range(len(guardconteudo)):

            def edit(r):

                altquart.place(x=700, y=50)
                altquart.config(text=f"Alterando: {guardconteudo[r].nome}")

                taltnm.place(x=700, y=100)
                altnome.place(x=700, y=150)
                taltpreco.place(x=700, y=200)
                altpreco.place(x=700, y=250)
                taltdispn.place(x=700, y=300)
                altdispn.place(x=700, y=350)

                altbtn = tk.Button(janela, text="Salvar ALterações", command= lambda r=r: alterquart(r))
                altbtn.place(x=800, y=400)
                grapc.append(taltnm)
                grapc.append(altquart)
                grapc.append(altnome)
                grapc.append(taltpreco)
                grapc.append(altpreco)
                grapc.append(taltdispn)
                grapc.append(altdispn)
                grapc.append(altbtn)


            def alterquart(y):

                guardconteudo[y].nome = altnome.get() 
                guardconteudo[y].preco = altpreco.get()

                if altdispn.get() == "S":

                    guardconteudo[y].dispn = "Disponível"
                    guardconteudo[y].ocpant = ""

                else:
                    guardconteudo[y].dispn = "Indisponível"
                    guardconteudo[y].ocpant = guardconteudo[y].ocpant


                with shelve.open('data/quartos.db') as db:

                    db.clear()

                    for f in range(len(guardconteudo)):

                        db[f"{f}"] = guardconteudo[f]

                # lamp()
                # limp()
                quats()

            listquart = tk.Label(main, font=("Arial", 16), text= f"{guardconteudo[y].nome} {guardconteudo[y].preco} {guardconteudo[y].dispn} {guardconteudo[y].ocpant}")
            listquart.place(x=50, y=50*(y+2))
            grap.append(listquart)

            listquartbtn = tk.Button(main, font=("Arial", 16), text="Alterar", command= lambda y=y: edit(y))
            listquartbtn.place(x=450, y=49*(y+2))
            grap.append(listquartbtn)


        altquart = tk.Label(main, font=("Arial", 16))
        taltnm = tk.Label(main, font=("Arial", 16), text="Nome:")
        altnome = tk.Entry(main)
        taltpreco = tk.Label(main, font=("Arial", 16), text="Preço:")
        altpreco = tk.Entry(main)
        taltdispn = tk.Label(main, font=("Arial", 16), text="Disponível:")
        altdispn = tk.Entry(main)












    botaoquartos = tk.Button(menu, width= 17, text="Quartos", command= quats)
    botaoquartos.place(x=10, y=50)

    txtqts = tk.Label(main, font=("Arial", 16), text="Quartos na Hospedagem:")


    


