def fatorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total
    
fac = int(input())
fac = fatorial(fac)
print(fac)
