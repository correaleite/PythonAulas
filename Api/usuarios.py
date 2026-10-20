import requests
import json

url = f'https://jsonplaceholder.typicode.com/users'

try:
    resposta = requests.get(url, verify=False)

    if resposta.status_code == 200:
            resposta_json = resposta.json()
            totalUser = 0
            usuarios = {}

            for user in resposta_json:
                lista_endereco = user['address']
                
                print('-'*50)

                print(f'Usuário: {user['username']}')
                usuario = user['username']

                print(f'Email: {user['email']}')
                email = user['email']

                print(f'Cidade: {lista_endereco['city']}')
                cidade = lista_endereco['city']

                totalUser += 1

                usuarios[user['id']] = {"usuario": usuario, "email": email, "cidade":cidade }
                usuariosJson = json.dumps(usuarios, indent=4, ensure_ascii=False) 
            print('-'*50)
            print(f'Total de usuários: {totalUser}')
    else:
        print('Erro de requisição!')
                
    with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write(usuariosJson)
            
except Exception as erro:
    print(f'Erro: {erro}')