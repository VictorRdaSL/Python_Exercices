cont = 0
soma = 0
while cont < 10:
    nota = float(input('Digite a nota: '))
    soma = nota + soma
    cont += 1
med = soma / 10

print('Sua média é: {}'.format(med))