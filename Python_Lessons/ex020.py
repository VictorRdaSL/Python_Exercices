#Faça um programa que peça o nome dos alunos que irão apresentar o trabalho e depois apresente os nomes de forma aleatória.

import  random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print ('A ordem de apresentação dos trabalhos será')
print (lista)

