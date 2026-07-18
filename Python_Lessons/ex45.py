mens = float(input('Digite o valor da mensalidade: '))

pag = int(input('Escolha uma das formas de pagamento - 1.Cartão  2.Pix  3.Dinheiro: '))

if pag == 1:
    print('No cartão você vai pagar {:.2f}reais sem descontos'.format(mens))
elif pag == 2:
   desc1 = (6*mens)/100
   desc6 = mens - desc1
   print('No PIX você vai pagar {:.2f}reais, com desconto de 6%({:.2f} reais)'.format(desc6,desc1))
elif pag == 3:
   desc1 = (10*mens)/100
   desc10 = mens - desc1
   print('No Dinheiro você vai pagar {:.2f}reais, com desconto de 10%({:.2f} reais)'.format(desc10,desc1))
else:
  print('Metodo não reconhecido, tente novamente!')