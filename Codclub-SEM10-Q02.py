from random import randint

jogando = True
score = 0

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

while jogando == True:

    novo_numero = randint(1, 10)

    score = score + novo_numero

    print(f'Seu próximo número é {novo_numero}')
    print(f'Sua pontuação agora é {score}')

    resposta = input('Gostaria de somar mais um número? (s/n): ').strip()
    if resposta.lower() == 'n' or score > 21:
        jogando = False

print(f'Sua pontuação final é {score}')

if score == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!")