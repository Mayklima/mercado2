#coding: utf-8

from estoque import cadastrar1
from estoque import vender1
from estoque import balanco1

class mercado1:
    def mercadoP(self):
        cadastro = cadastrar1()
        venda = vender1()
        balanc = balanco1()
        self.lista = []

        while True:
            print "==== Bem vindo(a) ao mercado====\n"
            print "Cadastrar um Produto: 1"
            print "Vender um Produto: 2"
            print "Imprimir Balanço: 3"
            print "Sair: 4"
            op = raw_input("\nOpcao: ")

            if op == "1":
                self.lista = cadastro.cadastrarProduto(self.lista)
            elif op == "2":
                self.lista = venda.venderProduto(self.lista)
            elif op == "3":
                self.lista = balanc.imprimirBalanco(self.lista)
            elif op == "4":
                print "\nObrigado!\nVolte Sempre!"
                break
            else:
                print "\nOpcao Invalida!!!\n"

mer = mercado1()
mer.mercadoP()