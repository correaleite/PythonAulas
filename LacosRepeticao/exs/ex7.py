n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

while n1 == n2:
    print("Números iguais são ínvalidos")
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))

if n1>n2:
   print(f"diferença entre {n1} e {n2}: {n1-n2}")
else:
    print(f"diferença entre {n1} e {n2}: {n2-n1}")