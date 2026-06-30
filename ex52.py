prod = float(input('Digite o valor do produto: '))
print (prod)
jur = ((prod*7)/100) + prod
parc = jur / 10
print ('Sua compra ficou no valor de {:.2f}. E terá que pagar 10 parcelas de {:.2f} reais'.format(jur,parc))
