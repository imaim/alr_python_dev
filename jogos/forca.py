def jogo_forca():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(f"iniciando Jogo")

        chute = str.lower(input("Digite uma letra "))
        index = 0
        for letra in palavra_secreta:
            if letra in chute:
                print(f"{chute} encontrada na posição {index}")
            index += 1


if __name__ == "__main__":
    jogo_forca()

