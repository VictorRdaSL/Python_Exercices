maior = 0
menor = 1000000000000000000000
fadase = 0
cont = 0

while cont < 3:
    a1 = int(input())
    if a1 > maior:
        maior = a1
    elif a1 < menor or a1 == 0:
        menor = a1
    else:
        fodase = a1
    cont +=1

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))