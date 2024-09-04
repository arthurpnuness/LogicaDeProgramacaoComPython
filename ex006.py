
## Instrução ao usuário 
print('Este código calcula a média e apovação de notas de um aluno!')

## Interação com o usuário
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

## Calculo
media = (nota1 + nota2) / 2

## Estruturas Condicionais e exibição do resultado
if media >= 7:
    print('Parabens {} voce foi aprovado com a nota final de {}'.format(nome, media))
else:
    print('{} infelizmente voce foi reprovado com a nota final de {}'.format(nome, media))