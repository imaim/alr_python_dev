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
            #print(numero_secreto)
            return numero_secreto
            break
        else:
            #print(numero_secreto)
            continue
        laco += 1


def numero(tent):

    #numero_secreto = randomico()
    numero_secreto = round(rd.randrange(1, 101))
    total_tentativas = tent

    for rodada in range(1, total_tentativas + 1):

        palpite = int(input("Digite seu palpite entre 1 e 100 ? "))
        errou = (palpite != numero_secreto)
        maior = (palpite > numero_secreto)
        menor = (palpite < numero_secreto)

        if 1 >= palpite < 100:
            print(f"Tentativa {rodada} de {total_tentativas}\n"
                  f"Erro - Você digitou {palpite}"
                  f"Digite um número entre 1 e 100")
            continue

        if errou:

            if rodada == total_tentativas:

                if maior:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Maior que o numero secreto \n"
                          f"Seu Ultimo Palpite foi {palpite} e o Número Secreto era {numero_secreto}")
                elif menor:
                    print(f"Tentativa {rodada} de {total_tentativas}\n"
                          f"Nao acertou, seu palpite foi Menor que o numero secreto \n" 
                          f"Seu Ultimo Palpite foi {palpite} e o Número Secreto era {numero_secreto}")
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
                  f"Acertou o Número Secreto {numero_secreto} !")
            break

        rodada += 1


numero(3)
print(f"Fim do Jogo")
