# jogando com score
from random import *
print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma dessas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
  _____      _____     _____
 |          | |           | |         |
 | [1]     | | [2]     | | [3]    |
 |    o    | |       o | |       o |
 |_____| |_____| |_____|
''')

score = 0
jogando = True
tent = 0

while jogando == True and score < 3:
    tent += 1
    print(f"Tentativa nº: {tent}\nEscolha uma porta (1, 2 ou 3):")
    porta_escolhida = input()
    porta_escolhida = int(porta_escolhida)
    porta_certa = randint(1,3)
    print("A porta escolhida foi a: ", porta_escolhida)
    print("A porta certa é: ", porta_certa)

    if porta_escolhida == porta_certa:
        print("Parabéns, você acertou!")
        score += 1
    else:
        print("Que pena! mais sorte na próxima")

    resposta = input('Deseja jogar novamente? (s / n): ').strip()
    if resposta.lower() in ('n', 'nao', 'não'):
        jogando = False

print('Obrigado por jogar!')
print("\nSua pontuação final foi de: ", score)
print(f'Terminou o jogo em {tent} tentativas')