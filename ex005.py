
## Instrução ao usuário
print('Neste código vamos calcular a área de uma sala, quarto e banheiro, somando as áreas para apresentar o total!!')

## Interação com o usuário
salaL = float(input('Largura da sala: '))
salaC = float(input('Comprimento da sala: '))
quartoL = float(input('Largura do quarto: '))
quartoC = float(input('Comprimento do quarto: '))
banheiroL = float(input('Largura do banheiro: '))
banheiroC = float(input('Comprimento do banheiro: '))

## Calculo das áreas
areaSala = salaL * salaC
areaQuarto = quartoL * quartoC
areaBanheiro = banheiroL * banheiroC
somaAreas = areaSala + areaQuarto + areaBanheiro

## Exibe o resultado da soma das áreas
print('A soma total das áreas é {}m²'.format(somaAreas))