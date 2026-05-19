import math

def bhaskara(a,b,c):
    if a == 0:
        if b == 0:
            print("Não possui raízes")
        else:
            print(f"A raíz é {-c/b}")
    elif b == 0:
        delta = -4*a*c
        x = math.sqrt(delta)
        print(f"A raíz é {x/(2*a)}") 
    elif c == 0:
        raiz1 = (-b + math.sqrt(b**2)) / (2*a)
        raiz2 = (-b - math.sqrt(b**2)) / (2*a)
        print(f"As raízes são {raiz1} e {raiz2}")
    else:
        delta = b**2-4*a*c
        x = math.sqrt(delta)
        raiz1 = (-b+x)/ (2*a)
        raiz2 = (-b-x)/ (2*a)
        print(f"As raízes são {raiz1} e {raiz2}")

    

print("Cálculo da fórmula de Bhaskara\n")
a = float(input("Informe o valor A: "))
b = float(input("Informe o valor B: "))
c = float(input("Informe o valor C: "))

bhaskara(a,b,c)

