'''
def nome_funcao(arg1:tipo, arg2:tipo, arg3:tipo) -> tipo_retorno
'''
def exibir_dados(nome:str, idade:int, altura:float) -> None:
    print(f'{nome} tem {idade} anos e {altura} de altura')

def somar_numeros(n1:float, n2:float) -> float:
    """ 
    Esta função recebe dois números float e
    retorna a soma desses dois números.

    Parâmetros: (float, float)
    Retorno: float
    """
    soma = n1 + n2
    return soma


# main()
exibir_dados('Paulo', 25, 1.71)

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
resultado = somar_numeros(n1,n2)
print(f'Resultado: {resultado}')