lista = [0]
cont = 0

while cont < 5:
    num = int(input())
    lista.append(num)
    lista.sort()
    cont += 1

print(lista)
