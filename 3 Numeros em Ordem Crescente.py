numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
valor = 0

if numero2 < numero1:
    valor = numero1
    numero1 = numero2
    numero2 = valor

if numero3 < numero1:
    valor = numero1
    numero1 = numero3
    numero3 = valor
    
if numero3 < numero2:
    valor = numero2
    numero2 = numero3
    numero3 = valor   

print(numero1)
print(numero2)
print(numero3)
