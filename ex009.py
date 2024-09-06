'''9. Calcular Salário com Aumento:
Desenvolva um programa que leia o total de horas trabalhadas no mês
e calcule o salário final de um funcionário que recebe R$35,00 por
hora. Caso o salário seja menor que R$1000,00, adicione um aumento
de R$300,00.'''

## Instrução ao usuário
print('Neste código vamos ver se voce tem direito a um aumento com base nas suas horas trabalhadas no mes!')

## Interação com o usuário
horasM = float(input('Quantas horas voce trabalha no mes? '))

## Calculo
salarioFinal = horasM * 35

## Estruturas Condicionais e exibição do resultado
if salarioFinal < 1000:
    aumento = salarioFinal + 1000
    print('Voce recebeu um aumento de R$1000,00 e agora seu passou para: R${}'.format(aumento))
else:
    print('Seu salario é de {}'.format(salarioFinal))