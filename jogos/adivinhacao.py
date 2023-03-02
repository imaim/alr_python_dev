import random as rd


print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")


def randomico():
    laco = 0
    numero_secreto = 0
    while laco >= 0:
        numero_secreto = round(rd.random() * 101)
        if 0 < numero_secreto <= 100:
            # print(numero_secreto)
            return numero_secreto
            break
        else:
            # print(numero_secreto)
            continue
        laco += 1


def numero():

    # numero_secreto = randomico()
    total_pontos = 1000
    numero_secreto = round(rd.randrange(1, 101))
    tent = int(input("Digite o nível de Dificuldade\n (1) Fácil - (2) Médio - (3) Difícil\n"))

    if 1 <= tent <= 3:
        if tent == 1:
            tentativa = 20
            delta = 0.5
        elif tent == 2:
            tentativa = 10
            delta = 1
        else:
            tentativa = 3
            delta = 2
    else:
        print("Dificuldade não identificada! \nDefinindo o modo Fácil por padrão")
        tentativa = 3

    total_tentativas = tentativa

    for rodada in range(1, total_tentativas + 1):

        palpite = int(input("Digite seu palpite entre 1 e 100 ? "))
        errou = (palpite != numero_secreto)
        maior = (palpite > numero_secreto)
        menor = (palpite < numero_secreto)

        # Trata palpite fora do range
        if palpite > 100:
            print(f"Tentativa {rodada} de {total_tentativas}\n"
                  f"Erro - Você digitou {palpite}"
                  f"Digite um número entre 1 e 100")
            continue

        # abs - nao deixa que seja numero negativo
        calq = abs(numero_secreto - palpite) * delta

        # evita valor negativo na pontuação
        if total_pontos > 0:
            total_pontos -= calq
        else:
            total_pontos = 0

        if errou:

            if rodada == total_tentativas:

                if maior:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Maior que o numero secreto \n"
                          f"Seu Ultimo Palpite foi {palpite} e o Número Secreto era {numero_secreto}\n"
                          f"Sua pontuação foi {total_pontos}")
                elif menor:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Menor que o numero secreto \n" 
                          f"Seu Ultimo Palpite foi {palpite} e o Número Secreto era {numero_secreto}\n"
                          f"Sua pontuação foi {total_pontos}")
            else:
                if maior:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Maior que o numero secreto \n"
                          f"Seu Ultimo Palpite foi {palpite}")
                elif menor:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Menor que o numero secreto \n" 
                          f"Seu Ultimo Palpite foi {palpite}")
        else:

            print(f"Tentativa {rodada} de {total_tentativas}\n"
                  f"Acertou o Número Secreto {numero_secreto}!\n"
                  f"Sua pontuação foi {total_pontos}")
            break

        rodada += 1


numero()
print(f"Fim do Jogo")
