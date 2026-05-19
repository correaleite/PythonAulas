def validar_nota(nota):
    while nota<0 or nota>10:
        print('Nota inválida, informe-a novamente')
        nota = float(input('Informe a nota válida: '))
        return nota
    
def status(n1, n2):
    media = (n1+n2)/2
    if media >= 6:
        print(f'Você foi aprovado, média: {media}')
    else:
        print(f'Você foi reprovado, média: {media}')

n1 = float(input('Informe a nota 1: '))
validar_nota(n1)
n2 = float(input('Informe a nota 2: '))
validar_nota(n2)

status(n1, n2)