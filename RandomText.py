import random
from gramatica import *
from anytree import Node, RenderTree
from anytree.exporter import DotExporter


class GeraOracao():
    def __init__(self):
        # inicilizando nossas váriveis
        # para efetuar os devidos armazenamentos
        self.frase = []
        self.arvore = []
        self.node = []
        g = Gramatica()
        self.iniciais = [pos for pos in g.gramatica]
        self.finais = [pos for pos in g.gramatica if len(pos) > 3]

    # função que vai gerar nossa oração
    # a partir da nosso módulo: gramatica
    # gerando nosso texto, de maneira 
    # randomica, e salvando para visualizar
    # futuramente na nossa interface
    def GeraOracao(self, pos):
        g = Gramatica()
        inicio = g.gramatica[pos]
        if pos == 'O':
            self.node.append(inicio)
        self.arvore.append(pos)
        if pos in self.finais:
            palavra = random.choice(inicio)
            self.frase.append(palavra)
            self.arvore.append(palavra)
            return
        for valor in inicio:
            if valor in self.iniciais:
                self.GeraOracao(valor)
            else:
                self.arvore.append(valor)
                #self.arvore.append([inicio, valor])
                self.frase.append(valor)

    # função para gerar manipular as palavras
    # identificando quem é o pai e o filho
    # para armazenar corretamente, e mostrar
    # na nossa interface gráfica
    def criaArvore(self, dot = True):
        try:
            inicio = Node('O')
            paiV = inicio
            paiR = inicio
            jaAdicionados = []
            for i in range(1, len(self.arvore)):
                if self.arvore[i] in self.node[0] and self.arvore[i] not in jaAdicionados:
                    paiV = Node(self.arvore[i], parent=inicio)
                    jaAdicionados.append(self.arvore[i])
                elif self.arvore[i] in self.iniciais:
                    paiR = paiV
                    paiV = Node(self.arvore[i], parent=paiV)
                else:
                    if self.arvore[i] == 'com' or self.arvore[i] == 'para':
                        Node(self.arvore[i], parent = paiV)
                    else:
                        Node(self.arvore[i], parent = paiV)
                        paiV = paiR
                if self.arvore[i] == 'CTN':
                    break
            if not dot:
                return RenderTree(inicio)
            else:
                DotExporter(inicio).to_dotfile('arvore.dot')
        except:
            return ''

