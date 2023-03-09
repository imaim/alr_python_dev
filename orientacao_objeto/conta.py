
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto.... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limit = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do Titular {self.titular}")

    def saca(self, valor):
        self.saldo -= valor
        print(f"Saldo {self.saldo} do Titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor
        print(f"Saldo {self.saldo} do Titular {self.titular}")
