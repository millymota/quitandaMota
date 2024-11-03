from flask import*

class Jogador:
    def __init__(self, id, nome, altura, time, camisa):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.time = time
        self.camisa = camisa

jogador = []
alterar = []

def addJogador(n, a, t, c):
    id = len(jogador) + 1
    jogador.append(Jogador(id, n, a, t, c))
    return jogador

def deleteJogador(id):
    for jogadores in jogador:
        if jogadores.id == id:
            jogador.remove(jogadores)
            return
        
def alterarJogador(id):
    for jogadores in jogador:
        if jogadores.id == id:
            return jogadores
        
def mudarJogador(n1,a1,t1,c1):
    if n1!='':
        jogador.nome = n1
    elif a1!='':
        jogador.altura = a1
    elif t1!='':
        jogador.time = t1
    elif c1!='':
        jogador.camisa = c1
    return jogador