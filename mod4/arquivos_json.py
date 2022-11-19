# Arquivo JSON
import json
from pathlib import Path
carros = [
    {"Marca":"Nissan","Preço":45.000,"Cor":"Azul"},
    {"Marca":"Ford","Preço":75.000,"Cor":"Verde"},
    {"Marca":"BMW","Preço":117.000,"Cor":"Amarelo"}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

arquivo_carros_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carros_json)
print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço'])) # Se for usar nome/marca mais numero/valor tem que tranforma em STR antes o numero/valor
print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço'])) # Se quiser adicionar espaço e so coloca + ' ' + 