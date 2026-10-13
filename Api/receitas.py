import requests

url = f'http://dummyjson.com/recipes?limit=50'

try:
    resposta = requests.get(url, verify=False)

    if resposta.status_code == 200:

        ing_busca = input('Ingrediente: ')

        resposta_json = resposta.json()

        lista_receitas = resposta_json['recipes']

        for receita in lista_receitas:
            lista_ingredientes = receita['ingredients']
            for ingrediente in lista_ingredientes:
                if ing_busca.lower() in ingrediente.lower():
                    print('-'*50)
                    print(receita['name'])
                    print(receita['ingredients'])
    else:
        print('Erro de requisição!')

except Exception as erro:
    print(f'Erro: {erro}')