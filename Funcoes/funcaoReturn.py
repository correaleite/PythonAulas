def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

#Main
b= int(input('Informe a base: '))
a = int(input('Informe a altura: '))

print(f'Área do triângulo: {calcular_area(b, a)}')