import random as rd

def jogar():

    print("\n ===================================")
    print("| Bem vindo ao jogo de Adivinhação! |")
    print(" ===================================")
    print("  Qual nível de dificuldade?")
    print("  (1) Fácil", "(2) Médio", "(3) Difícil", sep="\n  ")
    nivel = int(input("  Defina o nível: "))

    tentativas     = 3
    min_valor      = 1
    max_valor      = 10
    max_valor      = max_valor if nivel == 1 else (3*max_valor if nivel == 2 else 10*max_valor)
    numero_secreto = rd.randrange(1, max_valor+1)
    pontos         = 1000

    for rodada in range(1, tentativas + 1):
        print("\nTentativa {:03d} de {:03d}".format(rodada, tentativas))
        chute = int(input("Digite um número entre {1} e {0}: ".format(max_valor, min_valor)))
        
        if ( chute < min_valor or chute > max_valor):
            print("Você digitou {}. Está fora do intervalo permitido.".format(chute))
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if ( acertou ):
            print("=> Acertou! Parabéns, você terminou com {} pontos e ganhou R$ {:.2f}\n".format(pontos, 2))
            return
        elif ( maior ):
            print("=> Errrroooooouuu! Seu chute foi MAIOR que o número secreto.")
        elif ( menor ):
            print("=> Errrroooooouuu! Seu chute foi MENOR que o número secreto.")
        
        pontos -= abs(numero_secreto - chute)

    print("\n=> Fim de jogo. Você terminou com {} pontos e o número secreto era {}!".format(pontos, numero_secreto), end=2*"\n")


if ( __name__ == "__main__"):
    jogar()