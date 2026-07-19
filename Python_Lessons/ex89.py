a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print('É um Triângulo Equilatero')
elif a == c and b < a and b < c:
    print('É um Triângulo Isóceles')
elif a ==b and c > a and c > b:
    print('É um Triângulo Retângulo')
elif a != b and b != c:
    print('É um Triângulo Escaleno')
else:
    print('Deve ser outro tipo de triangulo')