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

from flask import Flask, jsonify, request

app = Flask(__name__)
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
    }
]

# Rota padrão - GET http://localhost:5000


@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET http://localhost:5000/postagem/1


@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_id(indice):
    return jsonify(postagens[indice], 200)

# Criar uma nova postagem - POST http://localhost:5000/postagem


@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# ALterar uma postagem existente - PUT   http://localhost:5000/postagem/0


@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE http://localhost:5000/postagem/0


@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)


app.run(port=5000, host='localhost', debug=True)
