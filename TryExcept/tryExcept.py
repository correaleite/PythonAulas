# Tratamento de erros e exceções

while True:
    try:
        n1 = int(input('Numerador: '))
        n2 = int(input('Denominador: '))

        result = n1/n2

        #validação
        if n1<0 or n2<0:
            raise TypeError

    except ValueError:
        print('Digite apenas números')
        print('Tente novamente\n')
    except ZeroDivisionError:
        print('Denominador deve der DIFERENTE de ZERO')
        print('Tente novamente\n')
    except TypeError:
        print('O valor informado é Negativo')
        print('Tente novamente\n')
    except Exception:
        print('Ocorreu um erro!\n')
    else:
        print(f'Resultado: {result:.2f}')
    finally:
        print('Tchau, Obrigado!')
