p = float(input ('Qual o preço do produto?: '))
d = 5*p
des = d/100
c = p-des
print('O valor desse produto com desconto é R${:.2f}'.format(c))