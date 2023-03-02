print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")


numero_secreto = 31


def numero(tent):

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
