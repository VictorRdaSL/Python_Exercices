#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.

nome = input(str('Qual seu nome completo?: ')).strip()
print('Seu nome tem silva?: ','silva' in nome.lower())
