class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo
