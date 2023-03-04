def jogo_forca():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    palavra_forca = ["_"] * len(palavra_secreta)

    print(f"iniciando Jogo")
    nivel = int(input("Selecione um Nível\n"
                      "(1) Fácil - (2) Médio (3) Difícil\n"))
    if nivel == 1:
        mult_nivel = 2
    elif nivel == 2:
        mult_nivel = 5
    else:
        mult_nivel = 2

    index_tent = 1

    while not enforcou and not acertou:

        # definicao de status para se enforcar ou nao
        # numero de tentativas igual ao tamanho da palavra
        tent = len(palavra_secreta) + mult_nivel

        if index_tent <= tent:
            if ''.join(palavra_forca) == palavra_secreta:
                print(f"Você acertou !!\n")
                acertou = True
                continue
            else:
                # Exibe tamnho da palavra
                print(f" Palavra # {' '.join(palavra_forca)}")

                chute = input(f"Tentativa {index_tent} de {tent}\n"
                              f"Digite uma letra\n")
                chute = chute.strip()
                chute = chute.lower()

                index = 0
                # Preenche Lista com acertos
                for letra in palavra_secreta:
                    if letra in chute:
                        palavra_forca[index] = chute
                    index += 1

        else:
            print(f"__Enforcado__\n"
                  f"A palavra era {palavra_secreta}")
            enforcou = True
            continue
            # break
        index_tent += 1
        print(f"Letra Encontrada \n Palavra # {' '.join(palavra_forca)}\n")


if __name__ == "__main__":
    jogo_forca()

