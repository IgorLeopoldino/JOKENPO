#import

import random
import time

#informações
'''
[0] PEDRA
[1] PAPEL
[2] TESOURA

'''
#variaveis

jogador = int(input("Qual sua jogada? "))
jogada = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)

print('-'*20) #linhas

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')

print('-'*20) #linhas

#janela de eventos

print('Computador escolheu {}'.format(jogada[computador]))
print('Jogador escolheu {}'.format(jogada[jogador]))

print('-'*20) #linhas

if jogador == 0: #JOGADOR ESCOLHEU PEDRA
    if computador == 0:
        print('Resultado: Empate')
    elif computador == 1:
        print('Resultado: Computador vence')
    elif computador == 2:
        print('Resultado: Jogador vence')
if jogador == 1: #JOGADOR ESCOLHEU PAPEL
    if computador == 0:
        print('Resultado: Jogador vence')
    elif computador == 1:
        print('Resultado: Empate')
    elif computador == 2:
        print('Resultado: Computador vence')
if jogador == 2: # JOGADOR ESCOLHEU TESOURA
    if computador == 0:
        print('Resultado: Computador vence')
    elif computador == 1:
        print('Resultado: Jogador vence')
    elif computador == 2:
        print('Resultado: Empate')
