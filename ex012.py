

# Inicializa as variáveis de contagem de tentativas e o limite máximo
num = 30
tentativas = 0
maxTentativas = 5

# Inicia o jogo
print('Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 0 e 50.')
print('Você tem {} tentativas.'.format(maxTentativas))

# Loop de tentativas, condições e resultado
while tentativas < maxTentativas:

    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == num:
     print('Parabens voce venceu o jogo com incriveis {} tentativa(s)'.format(tentativas))
     break
    elif palpite > num:
     print('O papite foi muito alto!')
    else:
     print('O palpite foi muito baixo:')

 # Verifica se atingiu o número máximo de tentativas
    if tentativas == maxTentativas:
        print('Você atingiu o número máximo de {} tentativas. O número secreto era {}.'.format(maxTentativas, num))
