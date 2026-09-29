import json

with open('foods.txt', 'r', encoding='utf-8') as arquivo:
    clientes = {}
    for linha in arquivo:
        dados = linha.split(",")
        name = dados[0]
        id = dados[1]
        favoritefodd = dados[2]

        clientes[id] = {"name": name, "food": favoritefodd}
    
with open('foods.json', 'w', encoding='utf-8') as arquivoJson:
    foodsJson = json.dumps(clientes, indent=4, ensure_ascii=False) 
    arquivoJson.write(foodsJson)