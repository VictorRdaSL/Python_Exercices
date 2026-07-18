termo = int(input('Digite o primeiro termo: '))
q = int(input('Digite a quantidade de termos: '))
r = int(input('Digite a razão: ' ))

for i in range(1,q+1):
    print("a",i,'...',termo)
    termo = termo + r