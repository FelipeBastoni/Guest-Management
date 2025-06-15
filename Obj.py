

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

