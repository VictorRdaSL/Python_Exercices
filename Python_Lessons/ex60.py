num  = []

num1 = int(input('Entre com um número: '))
num.append(num1)
print(num1)

while num1 != 0:
    num1 = int(input('Entre com um número: '))
    num.append(num1)

for n in num:
    num.sort()
    print(n)
    
if num1 == 0:
    print("End")
