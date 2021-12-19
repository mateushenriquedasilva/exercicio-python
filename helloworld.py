#print
print('hello world');
input()
#if else
if 2 > 1:
	print(True)
else:
	print(False)

#while
num = 1
num_2 = 10

while num <= num_2:
	print(num)
	num += 1

for i in range(num_2, 20, 2):
	print(i)

#function
def soma(num1, num2):
	return num1 + num2

print(soma(1, 2))