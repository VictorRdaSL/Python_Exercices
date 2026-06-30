# 09 - Manipulando Texto

frase = '   Curso em vídeo python  '
print(frase)
print(frase[6:19])
print(frase[::2])
print('Essa frase tem',len(frase), 'caracteres')
print('Na frase há',frase.count('o'),'letras "o"')
print (frase.find('y'))
print('py' in frase)

print(frase.replace('python','Cobol'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print ('-'.join(frase))

