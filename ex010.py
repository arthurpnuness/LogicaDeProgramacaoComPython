## instrução ao usuário
print('Vamos ver se voce tem acesso ao nosso programa empresarial, siga os passos')

## Interação com o usuário 
login = input('Digite seu login: ')
password = input('Digite sua senha: ')

## Estruturas Condicionais e exibição do resultado
if login == 'admin' and password == 'password':
    print('Acesso Liberado!')
else:
    print('Acesso Negado')
    