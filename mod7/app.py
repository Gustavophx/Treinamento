# Nosso 1º API  - Flask E Django
# FLASK & FLASK RESTFUL(Mais complexa)

'''
1 - Definir o objetivo do API:
    ex: Iremos monrat uma api de blog, onde eu poderei consultar, editar, criar, e excluir postagens em um blog usando a API

2 - Qual será o URL base do api?
    ex: QUando você cria uma aplicação local ela terá uma url tipo http://localhost:5000 , porém quando você for subir isso para nuvem, terá que 
    compra ou usar um domínio como url base, vamos imaginar um exemplo de devaprender.com/api/

3 - Quais são os endpoints?
    ex: Se seu requisito é de pode consultar, editar, criar e excluir, você terá que disponibilizar os endpoints para essas questões
            /postagens
4 - Quais recursos será disponibilizados pelo api: informações sobre as postagens

5 - Quais verbos http serão disponibilizados?
    * GET
    * POST
    * PUT
    * DELETE

6 - Quais são os URL completos para cada um?
    http://localhost:5000/postagens
'''

from flask import Flask, jsonify, request, make_response
from esturtura_BD import Autor, Postagem, app, db
import json
import jwt
from datetime import datetime,timedelta
from functools import wraps

postagens = [
    {
        'título': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'título': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    },
]
# Rota padrão - GET http://localhost:5000

def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None 
        # Verificar se um token foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'mensagem':'Token não foi incluído!'},401)
        # Se temos um token, validar acesso consultando o BD
        try:
            resultado = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'mensagem': 'Token é inválido'}, 401)
        return f(autor,*args,**kwargs)
    return decorated

@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login inválido', 401, {'WWW-Authenticate':'Basic raelm="Login obrigatório"'})
    usuario = Autor.query.filter_by(nome=auth.username).first()
    if not usuario:
        return make_response('Login inválido', 401,{'WWW-Authenticate':'Basic raelm="Login obrigatório"'})
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor':usuario.id_autor, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token})
    return make_response('Login inválido', 401,{'WWW-Authenticate':'Basic raelm="Login obrigatório"'})

@app.route('/')
@token_obrigatorio
def obter_postagens(autor):
    return jsonify(postagens)

# Obter postagem por id - GET http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
@token_obrigatorio
def obter_postagem_por_indice(autor, indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
@token_obrigatorio
def nova_postagem(autor):
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# ALterar uma postagem existente - PUT   http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['PUT'])
@token_obrigatorio
def alterar_postagem(autor, indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['DELETE'])
@token_obrigatorio
def excluir_postagem(autor, indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)

# http://localhost:5000/autores
@app.route('/autores')
@token_obrigatorio
def obter_autores(autor):
    autores = Autor.query.all() # Guarda a informação em uma variavel, "no caso autores = "
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    return jsonify({'autores': lista_de_autores})

@app.route('/autores/<int:id_autor>', methods=['GET'])
@token_obrigatorio
def obter_autor_por_id(autor, id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor não encontrado!')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email

    return jsonify({'autor': autor_atual}) # Formato utilizado para retorna em forma de lista, formatado. (dicionario)
   #return jsonify(f'Você buscou pelo autor: {autor_atual}')# formato que irar retornar em frase

@app.route('/autores', methods=['POST'])
@token_obrigatorio
def novo_autor(autor):
    novo_autor = request.get_json()
    autor = Autor(nome=novo_autor['nome'], senha=novo_autor['senha'], email=novo_autor['email'])

    db.session.add(autor)
    db.session.commit()

    return jsonify({'mensagem': 'Usuário criado com sucesso'}, 200)

@app.route('/autores/<int:id_autor>', methods=['PUT'])
@token_obrigatorio
def alterar_autor(autor, id_autor):
    usaurio_a_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({'Mensagem': 'Este usuário não foi encontrado'})
    try:
        autor.nome = usaurio_a_alterar['nome']
    except:
        pass
    try:
        autor.email = usaurio_a_alterar['email']
    except:
        pass
    try:
        autor.senha = usaurio_a_alterar['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'mensagem': 'Usuário alterado com sucesso!'})

@app.route('/autores/<int:id_autor>', methods=['DELETE'])
@token_obrigatorio
def excuir_autor(autor, id_autor):
    autor_existente = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor_existente:
        return jsonify({'mensagem': 'Este autor não foi encontrado'})
    db.session.delete(autor_existente)
    db.session.commit()

    return jsonify({'mensagem': 'Autor ecluído com sucesso!'})


app.run(port=5000, host='localhost', debug=True)
