import json

print("CADASTRO PETS\n 1.Inserir\n 2.Excluir\n 3.Listar Todos\n 4.Sair")
Menu = int(input("Escolha uma opção:"))

with open('pets.json', 'r', encoding='utf-8') as arquivo:
    pets = {}
    match Menu:
        case 1:
            print("oiii")
