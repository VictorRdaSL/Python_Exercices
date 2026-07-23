numeros = list(map(int, input().split()))

for passagem in range(len(numeros)):
    for i in range(len(numeros) -1):
        if numeros[i] > numeros[i + 1]:
            temp = numeros[i]
            numeros[i] = numeros[i + 1]
            numeros[i + 1] = temp
print(numeros)