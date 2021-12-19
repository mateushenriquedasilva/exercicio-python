numeros = input()
# a = '123.1 124.2'
numeros = numeros.split(" ")
numero1 = int(numeros[0])
numero2 = int(numeros[1])
if numero1 < numero2:
	print(f"{numero1:.2f} {numero2:.2f}")
else:
	print(f"{numero2:.2f} {numero1:.2f}")
