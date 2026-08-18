"""
DOCSTRING
- Tem como objetivo explicar o funcionamento de uma função
- É um comentário sempre localizado na 1a linha da função
- Deve estar entre 3 aspas duplas
- Contribuir para a documentação de um código fonte e melhorar o seu entendimento

ANOTAÇÕES DE TIPO
- Anotações de tipo (type hint) são utilizadas para indicar o tipo os tipos de dados das variáveis (parâmetros das funções)
- Objetivo: Tornar o código mais legível e organizado
"""
def somar(a:float, b:float) -> float:
    """
    Esta função realiza a soma de dois números do tipo float
    e retorna o resultado

    Parâmetros: (float, float)
    Retorno: float
    """
    return a + b

def media(a:int, b:int, c:int) -> float:
    """
    Está funções realiza a média aritmétrica de 3 números (int)
    e retorna o resultado
    """
    if type(a) == int and type(b) == int and type(c) == int:
        m = (a+b+c)/3
        return m
    else:
        print('Os valores devem ser do tipo int')
        return None

def entrada_dados() -> int:
    """
    Esta função permite o usúario digitar um número e retorná-lo
    """
    n = int(input('Número: '))
    return n

# Principal

resultado1 = somar(5,10)
print(f'Resultado: {resultado1}')
n1 = entrada_dados()
n2 = entrada_dados()
n3 = entrada_dados()
resultado2 = media(n1,n2,n3)
print(f'Média: {resultado2}')