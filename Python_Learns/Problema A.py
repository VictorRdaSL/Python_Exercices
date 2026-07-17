#PROBLEMA A - Uma questão similar ao INTERFATECS
# Um conjunto de três números naturais pode formar um triângulo se, para cada três números a, b e
# c, a soma de quaisquer dois números for maior que o terceiro. Por exemplo, o conjunto {3, 4, 5}
# pode formar um triângulo, mas o conjunto {1, 2, 5} não pode.
# Desenvolva um programa que, dado três números naturais, determine se eles podem formar um triângulo.
# triângulo.

# Entrada
# Três números naturais separados por espaço representando os comprimentos dos lados do triângulo.

# Saída
# Se os três números puderem formar um triângulo, imprima "Sim". Caso contrário, imprima "Não".


n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite outro numero: '))

if n1+n2 >= n3:
    print("sim")
else:
    print("não")
