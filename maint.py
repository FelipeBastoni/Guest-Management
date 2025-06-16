import tkinter as tk
import shelve
from datetime import datetime
from Obj import Quarto
import test
import abaregistroclientes
import abaquartos
import abaocuparquarto



#tkinter

janela= tk.Tk()
janela.title("HospedGerenctec")
janela.geometry("1000x600") 

menu = tk.Frame(janela, width=250, bg="lightblue")
menu.pack(side=tk.LEFT, fill=tk.Y)

main = tk.Frame(janela, width=700, bg="red")
main.pack(side=tk.RIGHT, fill="both", expand="true")

#Data e Hora
data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime("%d-%m-%Y - %H:%M:%S")
print(data_formatada)







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


























test.tela(janela)



abaregistroclientes.gregistro(menu, main, "oiii", janela)

abaquartos.abaquartos(janela, menu, main, guardconteudo, grapc, grap)














####Loads

with shelve.open("data/quartos.db") as db:

        for x in range(len(db)):

            conteudo = db[f"{x}"]
            guardconteudo.append(conteudo)


with shelve.open("data/Clientes.db") as db:

        for x in range(len(db)):

            pessoas = db[f"{x}"]
            clients.append(pessoas)


def atualizar_hora():

    HRA.clear()

    data_hora_atua = datetime.now()
    data_formatad = data_hora_atua.strftime("%d-%m-%Y - %H:%M:%S") 
    #janela.after(60000, atualizar_hora) #valor em mseg

    print(data_formatad)
    HRA.append(data_formatad)




#atualizar_hora() 
#PARA ATUALIZAR CONSTANTEMENTE

janela.mainloop()