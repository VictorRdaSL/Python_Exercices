d = float(input("Quantos dias você usou o carro ?: "))
k = float(input("Quantos KM você usou o carro ?: "))
pd = d * 60
kd = k * 0.15
v = pd + kd
print ('O total a pagar é de R$ {:.2f}'.format(v))

