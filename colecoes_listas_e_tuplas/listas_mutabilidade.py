# Objetos Métodos

class ContaCorrente:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'>>Codigo {self._codigo} Saldo {self._saldo} <<'



conta_do_gui = ContaCorrente(15)
conta_do_dani = ContaCorrente(453)
print(conta_do_gui)

conta_do_gui.deposita(1000)
print(conta_do_gui)

conta_do_dani.deposita(5000)
contas = [conta_do_gui, conta_do_dani]

print(contas)