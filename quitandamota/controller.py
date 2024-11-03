from flask import*
from model import*

jogadores_controller = Blueprint('jogadores', __name__)

@jogadores_controller.route('/')
def main():
    return render_template('index.html', jogador=jogador)

@jogadores_controller.route('/', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    altura = request.form['altura']
    time = request.form['time']
    camisa = request.form['camisa']
    jogador = addJogador(nome, altura, time, camisa)
    return render_template('index.html', jogador=jogador)

@jogadores_controller.route('/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    deleteJogador(id)
    return render_template('index.html', jogador=jogador)

@jogadores_controller.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    alterar = alterarJogador(id)
    return render_template('editar.html', id=alterar.id, nome=alterar.nome, altura=alterar.altura, time=alterar.time, camisa=alterar.camisa)

@jogadores_controller.route('/editar/<int:id>', methods=['PUT', 'POST'])
def alterar(id):
    nome1 = request.form['nome1']
    altura1 = request.form['altura1']
    time1 = request.form['time1']
    camisa1 = request.form['camisa1']
    jogador_novo = mudarJogador(nome1, altura1, time1, camisa1)
    jogador[id+1].update(jogador_novo)
    return render_template('index.html', jogador=jogador)
