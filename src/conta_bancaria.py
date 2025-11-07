class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor
