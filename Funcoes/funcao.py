"""def exibir_msg():
    print("Sejam Bem-vindos!")

#Main
for i in range(10):
    exibir_msg()
"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ínpar')

numero = int(input('Informe um número: '))
par_ou_impar(numero) #pode ser outra variavél no par_ou_inpar(N)