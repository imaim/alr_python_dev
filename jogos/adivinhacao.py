print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")


numero_secreto = 31


def numero(tent):

    total_tentativas = tent
    rodada = 1

    while 0 < rodada <= total_tentativas:

        palpite = int(input("Qual seu palpite para o numero Secreto ? "))
        errou = (palpite != numero_secreto)
        maior = (palpite > numero_secreto)
        menor = (palpite < numero_secreto)

        if errou:
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


numero(5)
print(f"Fim do Jogo")
