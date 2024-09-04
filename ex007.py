
## Instrução ao usuário 
print('Este calculo diz para o usuario se ja pode votar')

## Interação com o usuário
name = input('Digite seu nome: ')
year = int(input('Digite o seu ano de nascimento: '))

## Estruturas Condicionais e exibição do resultado
if year <= 2006:
    print('{}, voce ja pode votar!'.format(name))
else:
    print('{}, voce nao pode votar!'.format(name))