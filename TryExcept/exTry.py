'''
Calcular a densidade de um material com base em sua massa e volume. Fórmula: densidade = massa / volume
 1) Obter as medidas (massa e volume)
 2) Calcular a densidade com base na formula acima
 Restrições:
    -massa < 0 or volume < 0 | volume != 0
 3) Executar análise da densidade
    - função responsavel por executar as funções dos itens 1) e 2)
    - tratamento de exceções
'''

def obter_massa():
    massa = float(input('Massa do Material (em kg): '))
    return massa

def obter_volume():
    volume = float(input('Volume do Material (em m³: '))
    return volume

def calcular_densidade(massa:float, volume:float) -> float:
    if massa < 0 or volume < 0:
        raise ValueError("[ValueError]: Massa e Volume não podem ser negativos")

    if volume == 0:
        raise ZeroDivisionError("[ZeroDivisionError]: O Volume do material não pode ser ZERO")

    densidade = massa / volume

    return densidade

def executar_analise_densidade() -> None:

    try:
        massa = obter_massa()
        volume = obter_volume()

        densidade =  calcular_densidade(massa, volume)
    except ValueError as erro:
        print(f'[Erro de Entrada]: {erro}')
        print('Divisão por Zero impede o cálculo da densidade')
    except ZeroDivisionError as erro:
        print(f'[Erro Físico]: {erro}')
        print('Divisão por Zero impede o cálculo da densidade')
    else:
        print(f'\n [Sucesso]: Densidade do material: {densidade:.2f} em kg/m³')
    finally:
        print("--- Encerrando o calculo ---")

#main
while True:
    executar_analise_densidade()
    print('\n')