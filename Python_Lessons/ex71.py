print('A - Soma / B - Subtração / C - Multiplicação / D - Divisão')
choice = str(input()).upper()
if choice == 'A':
    print('opção SOMA')
    num1 = int(input())
    num2 = int(input())
    num3 = num1 + num2
    print(num3)

elif choice == 'B':
    print('opção SUBTAÇÃO')
    num1 = int(input())
    num2 = int(input())
    num3 = num1 - num2
    print(num3)

elif choice == 'C':
    print('opção MULTIPLICAÇÃO')
    num1 = int(input())
    num2 = int(input())
    num3 = num1 * num2
    print(num3)

elif choice == 'D':
    print('opção DIVISÃO')
    num1 = int(input())
    num2 = int(input())
    num3 = num1 / num2
    print("{:.2f}".format(num3))

else:
    print('opção invalida, tente novamente mais tarde!')
