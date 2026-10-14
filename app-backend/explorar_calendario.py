import json
import requests

url = "https://api.jolpi.ca/ergast/f1/current/races/"
resposta = requests.get(url)
resposta.raise_for_status()  # se der erro (404, 429...), para aqui e avisa

dados = resposta.json()
corridas = dados["MRData"]["RaceTable"]["Races"]

# 1) Veja a estrutura completa de UMA corrida
print(json.dumps(corridas[0], indent=2))

# 2) Veja uma lista resumida de todas
for corrida in corridas:
    print(corrida["round"], "-", corrida["raceName"], "-", corrida["date"])