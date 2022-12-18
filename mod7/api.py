# APIS são serviços disponibilizados online para acessar recursos ou funcionalidades de alguma aplicação web.
''' API possuem 4 partes. 
1. Url Base  EX: http://dummy.restapiexample.com/
2. Endpoint - O que vem depois do Url Base http://dummy.restapiexample.com/employees : no caso o employees e o ENDPOINT
Api são compostas de Url base + endpoint
3. Recurso  - Tudo o que é retornado ou enviado a uma api é considerado um recurso (resource em inglês)
4. Verbos HTTP 
GET - Obter dados existentes
POST - Enviar dados
PUT - Atualizar de dados existentes
DELETE - Excluir dados

### Status codes ###

1xx: Informação
2xx: Sucesso
3xx: Redirecionamento
4xx: Cliente error
5xx: Erro no servidor

Status codes na prática Apertar F12 em qualquer site e navegar até a aba "network"

'''
# Como usar 4 principais comandos (verbos HTTP) de uma API
import requests
from pprint import pprint

# Get
""" resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get.json()) """

# Get com id pra obter dado expecifico
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_com_id.json())

# Post - Criar um novo recurso
nova_tarefa = {'completed': False,
               'title': 'Lavar o carro',
               'userId': 1}
resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos',nova_tarefa)
pprint(resultado_post.json())

# Put - Alterar um recurso existente 
tarefa_alterada = {'completed': False,
                   'title': 'Lavar a moto',
                   'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
pprint(resultado_put.json())

# delete - Excluir um recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())


# Consultando APIs usando Postman


#como entra em um ambiente virtual ja criado ex: .\test\Scripts\activate