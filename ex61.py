#Estrutura de dados - Listas
numeros = [10,11,12,13,14,15,16]
num = int(input('Digite um número entre 10 e 16: '))

for i in range(0,7):
   if numeros[i] == num:
    numeros[i] = 7

for i in range(0,7):
  print(numeros[i])
