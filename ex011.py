

## Este código diz para o usuario o valor a pagar com desconto
print('Vamos ver quanto de desconto voce vai conseguir nas suas compras')

## Interação com o usuário
qtdProduto = int(input('Digite quantas camisetas voce quer adquirir: '))
preco = 10 
valorTotal = qtdProduto * preco

## Estruturas Condicionais, calculos e exibição do resultado
if qtdProduto <= 5:
    desconto1 = (qtdProduto * 10) * 0.02
    valorComDesconto = valorTotal - desconto1
    print('O valor a pagar com desconto é de R${}'.format(valorComDesconto))
elif qtdProduto >=6 and qtdProduto <= 10:
    desconto2 = (qtdProduto * 10) * 0.03
    valorComDesconto = valorTotal - desconto2
    print('O valor a pagar com desconto é de R${}'.format(valorComDesconto))
else:
    desconto3 = (qtdProduto * 10) * 0.05
    valorComDesconto = valorTotal - preco
    print('O valor a pagar com desconto é de R${}'.format(valorComDesconto))

