
## Instrução ao usuário 
print('Este código calcula a média de um aluno dizendo se ele foi aprovado ou reprovado!')

## Interação com o usuário
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Agora digite a nota da sua segunda nota: '))

## Calculo
media = (nota1 + nota2) / 2

## Estruturas Condicionais e exibição do resultado
if media >= 7:
    print('Parabens {} voce foi aprovado com a nota final de {}'.format(nome, media))
else:
    print('{} infelizmente voce foi reprovado com a nota final de {}'.format(nome, media))