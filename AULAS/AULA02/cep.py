import requests

cep = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"Você mora na {resposta["logradouro"]}. No bairro {resposta["bairro"]}. Na cidade de {resposta["localidade"]}")