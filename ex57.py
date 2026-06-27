cont = 0
val1 = 0
while cont < 7:
    val = int(input('Digite um número: '))
    cont += 1
    if val >= val1:
        val1 = val
    else:
        val1 = val1

print('O maior número digitado foi: {}'.format(val1))