n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

n4 = n1+n2+n3
n5 = n4 / 3


if (n5 >= 7):
    print('PARABÉNS, você foi aprovado ')
else:
    print('Reprovado')