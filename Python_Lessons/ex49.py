# Exercicio 49 - preço de dois produtos e desconto de 8% do primeiro e 11% do segundo e mostre o valor total a pagar

p1 = float(input())
p2 = float(input())

desc1 = (p1 * 8)/100
descp1 = p1 - desc1

desc2 = (p2 * 11)/100
descp2 = p2 - desc2
total = descp1 + descp2

print('Valor a ser pago com desconto é de {}'.format(total))