num = list(map(int, input().split()))
num2 = 0

for i in range(len(num)):
    if num[i] > num2:
         num2 = num[i]
    
for s in range(4):
    num[s] = num[s] * num2

print(f'{num[0]} {num[1]}\n{num[2]} {num[3]}')