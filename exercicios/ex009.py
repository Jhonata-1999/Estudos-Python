from random import randint
from time import sleep
computador = randint(0, 5)
print('--------' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('--------' * 30)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {})!'.format(computador, jogador))

