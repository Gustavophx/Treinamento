'''DESAFIO API músicas 🥇

### 1. Defnir o objetivo da API:
Iremos montar uma api de músicas, onde deverá ser possível, consultar todas canções disponíveis, 
consultar uma canção individual, editar canções existentes e também excluir músicas existentes.

### 2. Qual será o URL base da API?
Iremos utilizar o url base 'localhost'

### 3. Quais são os endpoints?
Disponibilize endpoints para consultar, editar, criar e excluir

### 4. Quais recursos serão disponibilizados pela API?
Informações sobre canções

### 5. Quais verbos http serão disponibilizados?
* GET
* POST
* PUT
* DELETE

### 6. Quais são os URLs completos para cada um?
* GET http://localhost:5000/cancoes
* GET http://localhost:5000/cancoes/1
* POST http://localhost:5000/cancoes
* PUT http://localhost:5000/cancoes/1
* DELETE http://localhost:5000/cancoes/1

### 7. Qual deve ser a estrutura de cada canção
- lista de dicionários, que contem cancao e estilo
'''

from flask import Flask, jsonify, request

app = Flask(__name__)
cancoes = [
    {
        'canção': 'Vicinity Of Obscenity',
        'estilo': 'Rock'
    },
    {
        'canção': 'Crazy',
        'estilo': 'Internacional'
    },
    {
        'canção': 'Unholy',
        'estilo': 'Lyrics'
    }
]

# Rota padrão - GET http://localhost:5000/cancoes
@app.route('/cancoes',methods=['GET'])
def obter_todas_cancoes():
    return jsonify(cancoes)

# Obter canção por id - GET http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>',methods=['GET'])
def obter_cancao_por_id(indice):
    return jsonify(cancoes[indice], 200)

# Criar uma nova canção - POST http://localhost:5000/cancoes
@app.route('/cancoes', methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A canção: {cancao} foi adicionada com sucesso', 200)

# ALterar uma postagem existente - PUT   http://localhost:5000/cancoes/0

@app.route('/cancoes/<int:cancao_id>',methods=['PUT'])
def alterar_cancao(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id],200)
    
# excluindo uma postagem existente - DELETE   http://localhost:5000/cancao/0
@app.route('/cancoes/<int:indice>',methods=['DELETE'])
def excluir_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify(f'Foi excluida a canção {cancoes[indice]}', 200)
    except:
        return jsonify('Não foi possivel encontrar a canção para exclusão', 404)


app.run(port=5000, host='localhost',debug=True)