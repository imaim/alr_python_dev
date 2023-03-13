
class Conta:
    def __init__(self, numero, titular, saldo, limit):
        print(f"Construindo Objeto.... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limit

    def extrato(self):
        print(f"Saldo {self.__saldo:.2f} do Titular {self.__titular}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"Saldo {self.__saldo:.2f} do Titular {self.__titular}")
        else:
            print(f"Saldo {self.__saldo:.2f} insuficiente do Titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Saldo {self.__saldo:.2f} do Titular {self.__titular}")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # getters
    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
