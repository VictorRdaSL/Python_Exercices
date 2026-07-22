soma = 0
cont = 0
num = int(input())

for i in range(0,num):
    if i % 2 == 0:
        continue
    else:
        soma = i + soma
        cont +=1
        print(i, ' -> ' ,soma)
        if soma == num:
            break
print('São {} impares'.format(cont))