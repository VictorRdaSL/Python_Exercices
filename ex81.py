def soma(n):
    total = 0
    for i in range (1, n + 1):
        total +=i
    return total

num = int(input())
res = soma(num)

print('total é {}'.format(res))