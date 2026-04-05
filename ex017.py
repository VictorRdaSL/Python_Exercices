import math
from xml.dom.minidom import ProcessingInstruction

print ('Vamos calcular a hipotenusa?')
num = float(input('Digite a altura: '))
num2 = float(input('Digite a base: '))

num3 = num*num
num4 = num2*num2
num5 = num3+num4
num6 = float(num5**0.5)

print ('A hipotenusa é: {:.2f}'.format(num6))