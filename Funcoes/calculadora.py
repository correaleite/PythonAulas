def adicao(n1, n2):
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    adicionar = n1 + n2
    return adicionar

def subtracao(n1, n2):
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    subtrair = n1 - n2
    return subtrair

def multiplicacao(n1, n2):
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    multiplicar = n1 * n2
    return multiplicar

def divisao(n1, n2):
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    dividir = n1 / n2
    return dividir

print('CALCULADORA:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair do programa')
opcao = int(input('Selecione sua opção: '))
n1 = 0
n2 = 0

def escolha_opcao(opcao):
    match opcao:
        case 1:
            print(f'Adição: {adicao(n1, n2)}')
        case 2:
            print(f'Subtração: {subtracao(n1, n2)}')
        case 3:
            print(f'Multiplicação: {multiplicacao(n1, n2)}')
        case 4:
            print(f'Divisão: {divisao(n1, n2)}')
        case 5:
            print('Calculadora fechada')

escolha_opcao(opcao)