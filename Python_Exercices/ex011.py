l = float(input('Qual a largura da parede em metros: '))
h = float(input('Qual a altura da parede em metros: '))
A = l*h
M = int(A/2)
print ('A parede mede {}m² e você vai precisar de {} litros de tinta'.format(A, M))
