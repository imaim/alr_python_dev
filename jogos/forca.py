def jogo_forca():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

    palavra_secreta = "paralelepipedo".lower()
    enforcou = False
    acertou = False
    #  palavra_forca = ["_" for letra in palavra_secreta]
    palavra_forca = ["_"] * len(palavra_secreta)

    print(f"iniciando Jogo")
    nivel = int(input("Selecione um Nível\n"
                      "(1) Fácil - (2) Médio (3) Difícil: "))
    if nivel == 1:
        mult_nivel = 4
    elif nivel == 2:
        mult_nivel = 2
    else:
        mult_nivel = 0

    erros = 0

    while not enforcou and not acertou:

        # definicao de status para se enforcar ou nao
        # numero de tentativas igual ao tamanho da palavra
        tent = len(palavra_secreta) + mult_nivel

        # Exibe tamnho da palavra
        print(f" Palavra # {' '.join(palavra_forca)}")

        chute = input(f"Digite uma letra: ")
        chute = chute.strip().lower()

        index = 0
        if chute in palavra_secreta:
            # Preenche Lista com acertos
            for letra in palavra_secreta:
                if letra in chute:
                    palavra_forca[index] = chute
                index += 1
        else:
            erros += 1

        acertou = "_" not in palavra_forca
        enforcou = erros == (6 + mult_nivel)

    if acertou:
        print("Você ganhou")
    else:
        print("Você perdeu")

    print("Fim do Jogo")


if __name__ == "__main__":
    jogo_forca()
