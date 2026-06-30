nome = str(input('Digite um nome: '))
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

med0 = n1+n2+n3
med = med0/3


if med >= 7:
    print('Parabéns {}!Você foi aprovado'.format(nome))

elif 7 >= med <= 5:
    print('Você ficou com média {} e está de recuperação'.format(med))
else:
    print('{}, você está reprovado'.format(nome))


