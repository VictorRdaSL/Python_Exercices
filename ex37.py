prod = float(input('Valor do produto: '))

desc0 = (10*prod) / 100
desc1 =  prod - desc0

print ('Seu produto custa {:.2f}, com desconto fica {:.2f}, você economizou {:.2f}'.format(prod,desc1,desc0))