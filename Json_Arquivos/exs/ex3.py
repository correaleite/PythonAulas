import json

with open('heroes.json', 'r', encoding='utf-8') as arquivo:
    herois = json.load(arquivo) 

    lista = herois["members"]
    
    for heroi in lista:
        linha_poderes = heroi["powers"]
        
        if "Flight" in linha_poderes :
            print(f'Nome: {heroi["name"]}')
            print(f'Poderes: {linha_poderes}')
            print('-'*40)

        
    