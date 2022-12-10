from requests.auth import HTTPBasicAuth
import requests

resultado = requests.get('http://localhost:5000/login',auth=('gustavo','123'))
print(resultado.json())