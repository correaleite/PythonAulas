def verificar_lados(nlados):
    while nlados < 3 or nlados > 5:
        print('Valor Inválido')
        nl = int(input('Informe novamente: '))


def ver_lados(nlados):
    match nlados:

        case 3:
            print('Triângulo')
        case 4:
            print('Quadrilátero')
        case 5:
            print('Pentágono')
        case _:
            print('Valor Inválido') 


nl = int(input('Informe o número de lados: '))
ver_lados(nl)
#verificar_lados(nl) verifica e pede dnv

