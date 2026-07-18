# Exercicio 49 - nome, duas nota e exiba média e aprovado ou reprovado se menor que 7


nome = str(input('Digite seu nome '))
nota1 = float(input())
nota2 = float(input())

med = (nota1 + nota2) / 2
if med >= 7:
    print ('Parabéns {} você foi aprovado!'.format(nome))
    print('fim')
else:
    print ('Você ficou com média {}  e foi reprovado'.format(med))
    print('fim')