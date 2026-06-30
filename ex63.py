med = float(input())
fre = int(input())


if fre >= 75 and med <= 7:
    print ('recuperação')

elif fre >= 75 and med >= 7:
    print('aprovado')
else:
    print('reprovado')