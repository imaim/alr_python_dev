import random as rd


def jogo_forca():

    imprime_msg_abertura()
    palavra_secreta = carregra_palavra_secreta()

    enforcou = False
    acertou = False
    #  palavra_forca = ["_" for letra in palavra_secreta]
    palavra_forca = inicializa_lista_palavra_secreta(palavra_secreta)

    print(f"iniciando Jogo")

    erros = 0

    while not enforcou and not acertou:

        # Exibe tamnho da palavra
        print(f" Palavra # {' '.join(palavra_forca)}")

        chute = solicita_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_forca, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        acertou = "_" not in palavra_forca
        enforcou = erros == 7

    if acertou:
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)


def imprime_msg_abertura():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")


def carregra_palavra_secreta():
    arquivo = open("palavras.txt", 'r')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = rd.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta


def inicializa_lista_palavra_secreta(palavra):
    return ["_"] * len(palavra)


def solicita_chute():
    chute = input(f"Digite uma letra: ")
    chute = chute.strip().lower()
    return chute


def marca_chute_correto(chute, palavra_forca, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if letra in chute:
            palavra_forca[index] = chute
        index += 1


def imprime_msg_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra}")
    print("    _______________         ")
    print("   /               \\       ")
    print("  /                 \\      ")
    print("//                   \\/\\  ")
    print("\\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \\__      XXX      __/     ")
    print("   |\\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \\_             _/       ")
    print("     \\_         _/         ")
    print("       \\_______/           ")


def imprime_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogo_forca()
