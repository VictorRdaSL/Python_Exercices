#Verificador de idade

from itertools import repeat

idade = int(input('Qual a sua idade?: '))

if idade <= 17:
    print ('Você é criança!')
elif idade <= 59:
    print('Você é ADULTO!')
else:
    print('Você é IDOSO!')

print('FIM')
