class ContaBancaria:
    def __init__(self):
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor do depósito deve ser maior que zero')
        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('Valor do saque deve ser maior que zero')
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor
