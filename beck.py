import tkinter as tk
import shelve
from datetime import datetime

#tkinter

janela= tk.Tk()
janela.title("HospedGerenctec")
janela.geometry("1000x600") 



#Data e Hora
data_hora_atual = datetime.now()
data_formatada = data_hora_atual.strftime("%d-%m-%Y - %H:%M:%S")
print(data_formatada)



#Classes
class Quarto:

    def __init__(self, nome, preco, dispn, ocpant):

        self.nome = nome
        self.preco = preco
        self.dispn = dispn
        self.ocpant = ocpant


    def __str__(self):

        return f"{self.nome}, {self.preco}, {self.dispn}, {self.ocpant}"


class Cliente:

    def __init__(self, rg, nomep, cll, divida):

        self.rg = rg
        self.nomep = nomep
        self.cll = cll
        self.divida = divida

    def __str__(self):

        return f"{self.rg}, {self.nomep}, {self.cll}, {self.divida}"




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
    button.place_forget()
    label.place_forget()
    selectquart.place_forget()
    selectbtn.place_forget()
    btntest.place_forget()
    ocptxt.place_forget()
    ocpent.place_forget()
    cadasbtn.place_forget()
    ocptxt2.place_forget()
    ocpent2.place_forget()
    ocpbtn.place_forget()
    rgent.place_forget()
    cllent.place_forget()
    ocpbtn.place_forget()
    txtcadast.place_forget()
    entrcadast.place_forget()
    entrcadast2.place_forget()
    btncadast.place_forget()
    buscr.place_forget()
    btnfech.place_forget()
    infofech.place_forget()
    abttxt.place_forget()
    abtdivida.place_forget()
    abtbtn.place_forget()
    tmpocpent.place_forget()
    tmpocptxt.place_forget()
    reg.place_forget()
    cncl.place_forget()
    txtqts.place_forget()
    rgtxt.place_forget()
    nomeptxt.place_forget()
    clltxt.place_forget()
    txtnm.place_forget()
    txtpr.place_forget()
    conca.place_forget()





#lista de quartos da hospedagem

def quats(): 

    fech()
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


            with shelve.open('quartos.db') as db:

                db.clear()

                for f in range(len(guardconteudo)):

                    db[f"{f}"] = guardconteudo[f]

            lamp()
            limp()
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





#reservando quarto

##função de ocupar quarto

def aa(p):

    if len(sla) == 0:
        popup = tk.Toplevel()
        popup.geometry("300x150")
        tk.Label(popup, text="Selecione um Cliente!", font=("Arial", 14)).pack(pady=20)
        tk.Button(popup, text="Fechar", command=popup.destroy).pack(pady=10)



    if guardconteudo[p].dispn == "Disponível" and sla[0].nomep != "":
        guardconteudo[p].ocpant = sla[0].nomep
        prec = int(tmpocpent.get())
        sla[0].divida = float(guardconteudo[p].preco)*prec
        guardconteudo[p].dispn = "indisponivel"


    with shelve.open('Clientes.db') as db:

        for i in range(len(db)):

            if db[f"{i}"].rg == sla[0].rg:

                del db[f"{i}"]
                db[f"{i}"] = sla[0]



    with shelve.open('quartos.db') as db:

        db.clear()

        for f in range(len(guardconteudo)):

            db[f"{f}"] = guardconteudo[f]



    with shelve.open("registro.db") as db:

        r = len(db)
        atualizar_hora()
        db[f"{r}"] = f"Quarto: {guardconteudo[p].nome}, Ocupado por: {guardconteudo[p].ocpant}, Valor: {guardconteudo[p].preco}\nData de entrada: {HRA[0]}, Estadia: {prec}"


    ocpquart()
    sla.clear()



##listando quartos

def ocpquart():

    fech()
    a = []

    for c in range(len(guardconteudo)):

        if guardconteudo[c].dispn == "Disponível":

            a.append(c)

    for b , c in enumerate(a):

            label = tk.Label(main, font=("Arial", 16))
            label.place(x=30, y=50*(b+2))
            grapc.append(label)

            button = tk.Button(main ,font=("Arial", 16), command= lambda c=c: aa(c), text="Ocupar")
            button.place(x=400, y=50*(b+2), width=80, height=30)
            grapc.append(button)

            label.config(text= f"{guardconteudo[c].nome} {guardconteudo[c].preco} {guardconteudo[c].dispn}")

    ocptxt.place(x=10, y=50)
    ocpent.place(x=10, y=100)
    selectbtn.place(x=10, y=150, width=150)
    btntest.place(x=330, y=240, width=120)
    buscr.place(x=10, y=200, width=300, height=80)
    tmpocpent.place(x=400, y=100, width=70)
    tmpocptxt.place(x=300, y=50)
    cadasbtn.place(x=10, y=300) #botão de cadastro
    selectquart.place(x=50, y=0)
    conca.pack(fill=tk.xy)



def busca():

    termo = ocpent.get().lower()
    buscr.delete(0, tk.END)
    a=0

    for pessoa in clients:

        if termo in pessoa.nomep.lower() or termo in pessoa.rg.lower():

            buscr.insert(tk.END, pessoa)
            a=1

    if a==0:
        buscr.insert(tk.END, "Cliente não encontrado")


##sincroniza o item selecionado com o objeto

def buscaselect():
    selected_index = buscr.curselection()

    if selected_index:

        sla.clear()
        sla.append(buscr.get(selected_index))

        if tmpocpent.get() == "":
            popup = tk.Toplevel()
            popup.geometry("300x150")
            tk.Label(popup, text="Preencha o Tempo de Estadia", font=("Arial", 14)).pack(pady=20)
            tk.Button(popup, text="Fechar", command=popup.destroy).pack(pady=10)
            sla.clear()

    crc = str(sla[0].split(',',1)[0])

    with shelve.open("Clientes.db") as db:

        for a in range(len(db)):

            if db[f"{a}"].rg == crc:

                s = db[f"{a}"]
                sla.clear()
                sla.append(s)





##aba de cadastro

def cadastroclient():

    if ocpbtn.winfo_ismapped():

        ocptxt2.place_forget()
        rgent.place_forget()
        ocpent2.place_forget()
        cllent.place_forget()
        ocpbtn.place_forget()
        rgtxt.place_forget()
        nomeptxt.place_forget()
        clltxt.place_forget()

    else:

        ocptxt2.place(x=10, y=350)
        rgtxt.place(x=10, y=400)
        rgent.place(x=90, y=400)
        nomeptxt.place(x=10, y=450)
        ocpent2.place(x=90, y=450)
        clltxt.place(x=10, y=500)
        cllent.place(x=90, y=500)
        ocpbtn.place(x=10, y=550)



#cadastra o cliente

def cadastrocli():


    pessoa = [ (rgent.get(), ocpent2.get(), cllent.get(), "")]


    for rg, nomep, cll, divida in pessoa:

        hospede = Cliente(rg, nomep, cll, divida)

        clients.append(hospede)

    rgent.delete(0, tk.END)
    cllent.delete(0, tk.END)
    ocpent2.delete(0, tk.END)


    with shelve.open("Clientes.db") as db:

        for x in range(len(clients)):

            db[f"{x}"] = clients[x]





#aba de fechamento

def fecha():

    fech()

    ocptxt.place(x=10, y=50)
    ocpent.place(x=10, y=100)
    selectbtn.place(x=10, y=150, width=150)
    buscr.place(x=10, y=200, width=300, height=80)
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





#aba de registro

def regs():

    fech()
    reg.place(x=10, y=50)

    with shelve.open("registro.db") as db:

        for a in range(len(db)):

            hist = tk.Label(janela, font=("Arial", 16), text=f"{db[f"{a}"]}", justify="left")
            hist.place(x=350, y=60*(a+2))
            grap.append(hist)









#####parte gráfica

menu = tk.Frame(janela, width=250, bg="lightblue")
menu.pack(side=tk.LEFT, fill=tk.Y)

main = tk.Frame(janela, width=700, bg="red")
main.pack(side=tk.RIGHT, fill="both", expand="true")



#ocupar quarto

conca = tk.Frame(janela, width=550, bg="lightblue")

botaoocp = tk.Button(menu, width= 15, text="Ocupar Quarto", command= ocpquart)
botaoocp.place(x=10, y=10)

ocptxt = tk.Label(main, font=("Arial", 16), text="Selecione o Cliente:")
tmpocptxt = tk.Label(main, font=("Arial", 16), text="Tempo de estadia:")
ocpent = tk.Entry(main, font=("Arial", 16))
tmpocpent = tk.Entry(main, font=("Arial", 16))
selectbtn = tk.Button(main, font=("Arial", 16), text="Buscar Cliente", command= busca)
btntest = tk.Button(main, font=("Arial", 16), text="Selecionar",command= buscaselect)
buscr = tk.Listbox(main, font=("Arial", 16))


##Cadastro de Clientes (opções que aparecem depois)

cadasbtn = tk.Button(main, font=("Arial", 16), text="Cadastrar Cliente", command= cadastroclient)
ocptxt2 = tk.Label(main, font=("Arial", 16), text="Aba de Cadastro:")

rgtxt = tk.Label(main, font=("Arial", 16), text="CPF:")
rgent = tk.Entry(main, font=("Arial", 16))
nomeptxt = tk.Label(main, font=("Arial", 16), text="Nome:")
ocpent2 = tk.Entry(main, font=("Arial", 16))
clltxt = tk.Label(main, font=("Arial", 16), text="Nº Tel")
cllent = tk.Entry(main, font=("Arial", 16))

ocpbtn = tk.Button(main, font=("Arial", 16), text="Cadastrar", command= cadastrocli)

##listagem de quartos no ocupar quarto

selectquart = tk.Label(main, font=("Arial", 16), text="Selecionar Quarto:")

label = tk.Label(main, font=("Arial", 16))
button = tk.Button(main, font=("Arial", 16))






#quartos

botaoquartos = tk.Button(menu, width= 17, text="Quartos", command= quats)
botaoquartos.place(x=10, y=50)

txtqts = tk.Label(main, font=("Arial", 16), text="Quartos na Hospedagem:")






#fechamento

botaofech = tk.Button(menu, width= 20, text="Fechamento de Clientes", command= fecha)
botaofech.place(x=10, y=90)

btnfech = tk.Button(main, text="Selecionar", font=("Arial", 16) ,command= bscfech)
infofech = tk.Label(main, text="", font=("Arial", 16))
abttxt = tk.Label(main, text="Valor a ser Abatido:", font=("Arial", 16))
abtdivida = tk.Entry(main, font=("Arial", 16))
abtbtn = tk.Button(main, font=("Arial", 16), text="Abater" ,command= abate)
cncl = tk.Button(main, font=("Arial", 16), text="Cancelar" ,command= cancel)






#registro de clientes

botaoreg = tk.Button(menu, width= 15, text="Registro de Clientes", command= regs)
botaoreg.place(x=10, y=130)

reg = tk.Label(main, font=("Arial", 16), text="Registro de Estadias:")











#gerenciamento

botaogeren = tk.Button(menu, width= 15, text="Adicionar Quarto", command= gerenc)
botaogeren.place(x=10, y=210)

txtcadast = tk.Label(main, text="Cadastro de quarto: ", font=("Arial", 16))
txtnm = tk.Label(main, text="Nome do Quarto:", font=("Arial", 16))
entrcadast = tk.Entry(main, width= 50)
txtpr = tk.Label(main, text="Preço do Quarto:", font=("Arial", 16))
entrcadast2 = tk.Entry(main, width= 20)
btncadast = tk.Button(main, text="cadastre", font=("arial",16), command= nvquarto)







####Loads

with shelve.open("quartos.db") as db:

        for x in range(len(db)):

            conteudo = db[f"{x}"]
            guardconteudo.append(conteudo)


with shelve.open("Clientes.db") as db:

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