import requests

url = "https://api.jolpi.ca/ergast/f1/current/races/"
resposta = requests.get(url)

print("Status:", resposta.status_code)
dados = resposta.json()
print(dados["MRData"]["total"], "corridas na temporada")