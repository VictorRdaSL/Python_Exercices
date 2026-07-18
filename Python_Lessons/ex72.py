cont = 0
maior = 0
menor = 100000000
soma = 0

while cont < 10:
    num = int(input())
    soma = num + soma
    
    cont += 1
    
    if num <= menor:
        menor = num
        
    if num >= maior:
        maior = num

med = soma / 10
        
print("-------------")
print(maior)
print(menor)
print(soma)
print ('{:.2f}'.format(med))
