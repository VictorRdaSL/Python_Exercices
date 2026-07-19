user = str(input('Digite o seu usuário: '))

pas = str(input('Digite sua senha: '))

while pas == user:
    print('A senha não pode ser igual ao nome de usuário!!')
    pas = str(input('Digite sua senha novamente: '))

print ('Bem-vindo')