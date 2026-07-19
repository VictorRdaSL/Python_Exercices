a = input()
b = ''

for i in range(0, len(a) -1,2):
    b += a[i +1] + a[i]

if len(a) % 2 != 0:
    b += a[-1]
print(b)