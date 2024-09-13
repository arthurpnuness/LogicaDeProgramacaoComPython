
## Instrução ao usuário
print('Neste código vamos te ajudar a descobrir o custo do consumidor apartir do custo de fabrica de um veiculo. Por favor siga os passos!')

## Interação com o usuário
custoFabrica = float(input('Qual foi o custo de fabrica do veiculo? '))

## Calculos
percentualDistri = custoFabrica * 0.28 
imposto = custoFabrica * 0.45
custoConsumidor = custoFabrica + percentualDistri + imposto

## Exibe o resultado
print('O custo do consumidor é de R$ {}'.format(custoConsumidor))
