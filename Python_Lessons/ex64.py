num = []

while True:
    num1 = int(input())
    num2 = num1 % 2
    if num1 == 0:
        break
    if num2 == 0:
        num.append(num1)

print('----')

for n in num:
    print(n)