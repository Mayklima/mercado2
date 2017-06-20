class produto1:
    def __init__(self, nome, preco, tipo, quantidade):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.quantidade = quantidade

    def getNome(self):
        return self.nome
    def getPreco(self):
        return self.preco
    def getTipo(self):
        return self.tipo

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self,quantidade2):
        self.quantidade = quantidade2
