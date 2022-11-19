import json
from pathlib import Path

pikachu_json = Path('pikachu.json').read_text()
ability = json.loads(pikachu_json)
print(ability['abilities'][1]['ability']['name'])


# Arquivo 'Pikachu.json' movido pois não foi eu que escrevi.