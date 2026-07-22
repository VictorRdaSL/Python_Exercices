num = int(input())

num = str(num)
num4 = len(str(num))

num1 = num[0]
num2 = num[1]
num3 = num[2]

if num4 == 4:
    num1 = 10

print('{} centenas, {} dezenas e {} unidades'.format(num1,num2,num3))