alt = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))

imc = peso / (alt * alt)

print(imc)
if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso normal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30:
    print('Obesidade')
else:
    print('Error')