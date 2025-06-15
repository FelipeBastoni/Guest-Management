import tkinter as tk
import shelve 
from Obj import *
from datetime import datetime



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




janela= tk.Tk()
janela.title("HospedGerenctec")
janela.geometry("1000x600") 

menu = tk.Frame(janela, width=250, bg="lightblue")
menu.pack(side=tk.LEFT, fill=tk.Y)

main = tk.Frame(janela, width=700, bg="red")
main.pack(side=tk.RIGHT, fill="both", expand="true")





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
    btnfech.place_forget()
    infofech.place_forget()
    abttxt.place_forget()
    abtdivida.place_forget()
    abtbtn.place_forget()
    cncl.place_forget()








#aba de fechamento

def fecha():

    fech()

    btnfech.place(x=170, y=150)
    infofech.place(x=600, y=70)
    abttxt.place(x=450, y=200)
    abtdivida.place(x=650, y=200)
    abtbtn.place(x=820, y=250)
    cncl.place(x=800, y=300)


def bscfech():
    selected_index = buscr.curselection()

    if selected_index:

        sla.clear()
        sla.append(buscr.get(selected_index))

    crc = str(sla[0].split(',',1)[0])


    with shelve.open("Clientes.db") as db:

        for a in range(len(db)):

            if db[f"{a}"].rg == crc:

                s = db[f"{a}"]
                sla.clear()
                sla.append(s)

    infofech.config(justify="left" ,text= f"Nome: {sla[0].nomep}\nRg: {sla[0].rg}\nDivida: {sla[0].divida}R$")


def abate():
    valor = abtdivida.get()

    vl = float(valor)

    with shelve.open("Clientes.db") as db:

        for p in range(len(db)):

            if db[f"{p}"].rg == sla[0].rg:

                if sla[0].divida >= vl:

                    sla[0].divida = sla[0].divida - vl
                    del db[f"{p}"]
                    db[f"{p}"] = sla[0]
                    clients.clear()

                    for x in range(len(db)):

                        pessoas = db[f"{x}"]
                        clients.append(pessoas)

                    buscr.delete(0, tk.END)
                    abtdivida.delete(0, tk.END)
                    infofech.config(text="")

                else:

                    print("invalido")



def cancel():

    clients.clear()

    with shelve.open("Clientes.db") as db:

        for x in range(len(db)):
            pessoas = db[f"{x}"]
            clients.append(pessoas)

    buscr.delete(0, tk.END)
    abtdivida.delete(0, tk.END)
    infofech.config(text="")


#fechamento

botaofech = tk.Button(menu, width= 20, text="Fechamento de Clientes", command= fecha)
botaofech.place(x=10, y=90)

btnfech = tk.Button(main, text="Selecionar", font=("Arial", 16) ,command= bscfech)
infofech = tk.Label(main, text="", font=("Arial", 16))
abttxt = tk.Label(main, text="Valor a ser Abatido:", font=("Arial", 16))
abtdivida = tk.Entry(main, font=("Arial", 16))
abtbtn = tk.Button(main, font=("Arial", 16), text="Abater" ,command= abate)
cncl = tk.Button(main, font=("Arial", 16), text="Cancelar" ,command= cancel)


janela.mainloop()