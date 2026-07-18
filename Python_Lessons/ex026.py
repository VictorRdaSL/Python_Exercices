#Faça um programa que leia a frase pelo teclado e mostre: quantas vezes a letra a aparece, em qual posição aparece a primeira vez, e posição da ultima vez.

frase = str(input('Digite uma frase: ')).strip().lower()
print('Essa frase tem {} letras A'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('E aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))