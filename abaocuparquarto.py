import tkinter as tk
import shelve
from datetime import datetime
from Obj import *











def abaocuparquarto(sla, guardconteudo, clients, atualizar_hora, HRA, grapc, main, menu, janela):

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


    #função fechar
    def fech():

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
        buscr.place_forget()
        tmpocpent.place_forget()
        tmpocptxt.place_forget()
        rgtxt.place_forget()
        nomeptxt.place_forget()
        clltxt.place_forget()
        conca.place_forget()


