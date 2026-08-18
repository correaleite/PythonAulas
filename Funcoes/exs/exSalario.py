"""
Exercício 1
Escreva um programa em Python para calcular o salário de um funcionário.
 Implemente uma função calcular_salário e permite receber o salário atual
 de um funcionário e retornar o salário com reajuste de aumento, sendo que:
 - caso o salário seja maior que R$2000, recebe 7% de aumento
 - caso contrário, recebe 15% de aumento
"""

def calcular_salario(salario:float) -> float:
    """
    Recebe o salario (float) e o retorna com reajuste de aumento, 
    se o salario for maior que R$2000 o aumento é de 7%,
    caso contrário, recebe 15% de aumento 
    """
    if salario > 2000:
        return salario * 0.07 + salario
    else:
        return salario * 0.15 + salario

def entrada_dados():
    """
    Esta função permite o usúario digitar o seu salário e retorná-lo
    """
    n = int(input('Digite o seu salário: '))
    return n

salario = entrada_dados()
resultado = calcular_salario(salario)
print(f'Salario reajustado: R${resultado} | era: R${salario}')