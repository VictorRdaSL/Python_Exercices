def calcular_area(l,c):
    a = l * c
    return a

#Execução do código

larg = int(input('Digite a largura do terreno em metros: '))
comp = int(input('Digite o comprimento do terreno em metros: '))

res = calcular_area(larg,comp)

print('A área do terreno é {} metros quadrados'.format(res))
