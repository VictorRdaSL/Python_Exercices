sal = float(input('Quanto você recebe ?: '))

if (sal  <= 500):
    sal1 = (15*sal) /100
    sal15 = sal1 + sal
    print("Seu reajuste é de 15%: {}".format(sal15))

elif (sal >= 501 <= 1000 ):
    sal2 = (10*sal) /100
    sal10 = sal2 + sal
    print("Seu reajuste é de 10%: {}".format(sal10))
else:
    sal3 = (5*sal)/100
    sal5 = sal3 + sal
    print("Seu reajuste é de 5%: {}".format(sal5))