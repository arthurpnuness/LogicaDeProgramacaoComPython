'''Verificação de Login e Senha:
Escreva um programa que solicite o login e a senha do usuário. Se o
login for "admin" e a senha for "password", exiba "Acesso liberado",
caso contrário, exiba "Acesso negado".'''

login = input('Digite seu login: ')
password = float(input('Digite sua senha: '))

if login == 'admin':
    print('Acesso liberado')
elif password == 'password':
    