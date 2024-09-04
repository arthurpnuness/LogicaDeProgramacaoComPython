
## Instrução ao usuário 
print('Este é um programa que conscientiza o motorista (apartir dos valores das multas) a nao infrigir as regras de transito e evitar acidentes')

## Interação com o usuário
print('Mais de 120 km/h: A')
print('MAis de 100 km/h: B')
print('Mais de 80 km/h: C')
opcao = input('Qual a opcao desejada: ')

## Estruturas Condicionais e exibição do resultado
if opcao == 'A':
    print('Multa de R$1000,00 e 7 pontos na carteira.')
elif opcao == 'B':
    print('Multa de R$750,00 e 5 pontos na carteira.')
else:
    print('Multa de R$500,00 e 4 pontos na carteira.')
