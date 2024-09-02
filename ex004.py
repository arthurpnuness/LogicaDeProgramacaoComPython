
## Instrução ao usuário
print('Neste código vamos descobrir em qual das categorias voce se enquandra com base na sua idade. Siga os passos a seguir.')

## Interação com o usuário
idade = int(input('Digite sua idade: '))

# Estruturas de controle e resultados
if (idade >= 5) and (idade <= 7):
    print('Voce faz parte da Categoria Infantil A (5-7 anos)')
elif (idade >= 8) and (idade <= 10):
    print('Voce faz parte da Categoria Infantil B (8-10 anos)')
elif (idade >= 11) and (idade <= 13):
    print('Voce faz parte da Categoria Juvenil A (11-13 anos)')
elif (idade >= 14) and (idade <= 17):
    print('Voce faz parte da Categoria Juvenil B (15-17 Anos)')
else:
    print('Voce faz parte da Categoria Adulto (maior de 18 anos)')