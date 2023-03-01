print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

palpite = input("Qual seu palpite para o numero Secreto ?")


class NumeroTest:
    def __init__(self, numero):
        self.valor = numero
        while self.valor != numero_secreto:
            return print("Voce não acertou")
        return print("Voce acertou")


print(NumeroTest(palpite))
