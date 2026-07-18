while True:
    num = int(input())

    if 0 <= num <= 25:
        print('Esse número está no intervalo [0-25]')
    elif 26 <= num <= 50:
        print('Esse número está no intervalo [26-50]')
    elif 51 <= num <= 75:
        print('Esse número está no intervalo [51-75]')
    elif 76 <= num <= 100:
        print('Esse número está no intervalo [76-100]')
    elif num > 100:
        print('Esse número não está nos intervalos')
    elif num == 0:
        break
    else:
        print('para de inventar moda')