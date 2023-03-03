from adivinhacao import jogo_adivinhacao
from forca import jogo_forca

print("********************************")
print("Bem vindo ao Seletor de Jogos")
print("********************************")

jogo = int(input("Selecione o jogo \n (1) Forca - (2) Advinhacção\n"))

if jogo == 1:
    print("Iniciando jogo da Forca")
    jogo_forca()
elif jogo == 2:
    print("iniciando Jogo de Advinhação")
    jogo_adivinhacao()
