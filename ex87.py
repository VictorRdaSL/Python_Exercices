cont = 0
notas = 0
f = 0

while cont < 3:
    n = int(input())
    cont +=1
    notas = n + notas
    if cont == 1:
        f = (n * 2) + f
    elif cont == 2:
        f = (n * 3) + f
    elif cont == 3:
        f = (n * 5) + f

let = str(input()).upper()
if let == 'A':
    med = notas / 3
    print('Sua média é {}'.format(med))
elif let == 'P':
    pond = f / 10
    print('Sua média ponderada é {}'.format(pond))