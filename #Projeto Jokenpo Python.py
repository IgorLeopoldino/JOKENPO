#import

import random
import time

#informações
'''
- INÍCIO;
- JOGAR / O QUE É "JOKENPO?"

JOGAR:
[0] PEDRA
[1] PAPEL
[2] TESOURA

'''
print('-='*10 + 'BEM-VINDO AO JOKENPÔ' + '-='*10)

time.sleep(2)

#variaveis

escolha = int(input('Qual sua escolha?\n[0] Jogar\n[1] Saiba mais sobre o jogo\n--> '''))

time.sleep (1)

if escolha == 0:
    print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')

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
elif escolha == 1:
    print('''Pedra, papel e tesoura, também chamado em algumas regiões do Brasil de jokenpô, é um jogo de mãos recreativo e simples para duas ou mais pessoas, que não requer equipamentos nem habilidade. O jogo é frequentemente empregado como método de seleção, assim como lançar moedas, jogar dados, entre outros.''')