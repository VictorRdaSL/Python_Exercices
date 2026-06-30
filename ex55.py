cont = 0
soma = 0
qnota = int(input('Quantas notas seriam?: '))
while cont < qnota:
    nota = float(input('Qual a nota?: '))
    soma = soma + nota
    cont +=1
soma2 = soma / cont

print('Sua média é {}'.format(soma2))
