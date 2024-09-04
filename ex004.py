
## Instrução ao usuário
print('Neste código vamos descobrir em qual das categorias voce se enquandra com base na sua idade. Siga os passos a seguir.')

## Interação com o usuário
age = int(input('Digite sua idade: '))

# Estruturas de controle e resultados
if (age >= 5) and (age <= 7):
    print('Voce faz parte da Categoria Infantil A (5-7 anos)')
elif (age >= 8) and (age <= 10):
    print('Voce faz parte da Categoria Infantil B (8-10 anos)')
elif (age >= 11) and (age <= 13):
    print('Voce faz parte da Categoria Juvenil A (11-13 anos)')
elif (age >= 14) and (age <= 17):
    print('Voce faz parte da Categoria Juvenil B (15-17 Anos)')
else:
    print('Voce faz parte da Categoria Adulto (maior de 18 anos)')