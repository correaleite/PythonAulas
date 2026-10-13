# pip install requests  (API CEP)
import requests

'''
1) Obter CEP
2) Receber CEP (1) e realizar a requisição
3) Imprimir os dados recebidos
'''

def obter_cep():
    cep = input('Digite um CEP: ')
    url = f'https://viacep.com.br/ws/{cep}/json/'
    return url

def realizar_requisicao(url):
    requisicao = requests.get(url)
    return requisicao

def imprimir_cep(requisicao):
    try:
        if requisicao.status_code == 200:
            resposta_json = requisicao.json()

            print(f'CEP: {resposta_json['cep']}')
            print(f'Logradouro: {resposta_json['logradouro']}')
            print(f'Complemento: {resposta_json['complemento']}')
            print(f'Bairro: {resposta_json['bairro']}')
            print(f'Localização: {resposta_json['localidade']}')
            print(f'Estado: {resposta_json['uf']}')

        elif requisicao.status_code == 404:
            print('Não foi possível encontrar o endereço')
        elif requisicao.status_code == 500:
            print('Ocorreu algum erro no Servidor')
        else:
            print(requisicao.status_code)
    except ConnectionError as e:
        print(f'Houve um erro de conexão: {e}')
    except Exception as e:
        print(f'Erro: {e} ')


url = obter_cep()
requisicao = realizar_requisicao(url)
imprimir_cep(requisicao)
