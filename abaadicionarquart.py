import tkinter as tk
import shelve
from Obj import *
from datetime import datetime


janela= tk.Tk()
janela.title("HospedGerenctec")
janela.geometry("1000x600") 

menu = tk.Frame(janela, width=250, bg="lightblue")
menu.pack(side=tk.LEFT, fill=tk.Y)

main = tk.Frame(janela, width=700, bg="red")
main.pack(side=tk.RIGHT, fill="both", expand="true")



data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime("%d-%m-%Y - %H:%M:%S")
print(data_formatada)

def atualizar_hora():

    HRA.clear()

    data_hora_atua = datetime.now()
    data_formatad = data_hora_atua.strftime("%d-%m-%Y - %H:%M:%S") 
    #janela.after(60000, atualizar_hora) #valor em mseg

    print(data_formatad)
    HRA.append(data_formatad)






#memória de dados
sla = []
#incluir quarto
quartos = []
#save de quartos
guardconteudo = []
#para limmpar content criado por interação
grapc = []
grap = []
#guardar clientes
clients = []
#save de horário
HRA = []


#limpador de elementos gerados por interação
def limp():

    global grapc

    for gr in grapc:

        gr.place_forget()

    grapc.clear()


def lamp():

    global grap

    for gr in grap:

        gr.place_forget()

    grap.clear()



#função fechar
def fech():

    lamp()
    limp()
    txtcadast.place_forget()
    entrcadast.place_forget()
    entrcadast2.place_forget()
    btncadast.place_forget()
    txtnm.place_forget()
    txtpr.place_forget()




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



janela.mainloop()