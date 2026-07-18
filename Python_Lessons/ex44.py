letra = str(input('Digite uma letra: ')).lower()

#if len(letra) != 1 or not letra.isalpha():
if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')