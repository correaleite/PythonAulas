import requests

cont = 1
url = 'http://pokeapi.co/api/v2/pokemon'

response = requests.get(url)

dados = response.json()

lista = dados['results']

for pokemon in lista:
    print(f'{cont}) {pokemon['name']}')
    cont+=1