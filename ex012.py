'''12. Adivinhação de Número:
Crie um jogo onde o usuário deve adivinhar um número aleatório entre
0 e 50. O programa deve informar se o palpite é muito alto ou baixo e
contar o número de tentativas. Informe o jogador se ele quebrou o
recorde de tentativas.'''


def maior(num):
    if num > 30:
        return 'Esta perto! O numero correto é menor'
    else:
        return 'Voltando para voce descobrir o numero...'


def menor(num):
        if num < 30:
            return 'Está perto! O numero correto é maior '
        else:
            return 'Voltando para descobrir o numero...'
    

def opcaoCorreta(num):
    if num == 30:
        print('Voce acertou Parabens o numero correto é {}'.format)

tentativas = 0

while True:
    num = int(input('Digite um numero entre 0 e 50: '))
    tentativas += 1





