#Programa que lê um nome completo e mostre esse nome com todas as letras maiúsculas , letras minísculas, quantas letras
#aotodo (sem espaços) e quantas letras no primeiro nome.

nome = str(input('Digite seu nome completo:')).strip()
separa = nome.split()
print('Esse é seu nome com todas as letras MAIÚSCULAS: {} '.format(nome.upper()))
print('Esse é seu nome com todas as letras minúsculas: {} '.format(nome.lower()))
print('Seu nome tem: {} letra(s)'.format(len(nome) - nome.count(' ')))
#print('Seu primero nome tem: {} letra(s)'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letra(a)'.format(separa[0], len(separa[0])))


