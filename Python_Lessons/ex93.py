a = str(input()).lower()
a2 = a.replace(' ','')
inv = a2[::-1]
if a2 == inv:
    print(a,'É um palíndromo')
else:
    print(a, 'Não é um palíndromo')
