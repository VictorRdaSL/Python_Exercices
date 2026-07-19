#Ao Digitar um numero o programa vai mostrar o FIBONACCI  da posição deste numero.

cont = 0 
a = 1
b = 1

n = int(input())
print('1')
print('1')
while cont < (n / 2) - 1:
    b = a + b
    print(b)
    a = b + a
    print (a)
    cont +=1