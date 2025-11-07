class ContaBancaria:
    def __init__(self):
        self._saldo = 0.0

    @property
    def saldo(self):
        return self._saldo

    def _validar_valor(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('Valor deve ser numérico')
        if valor <= 0:
            raise ValueError('Valor deve ser maior que zero')
        return float(valor)

    def depositar(self, valor):
        valor = self._validar_valor(valor)
        self._saldo += valor

    def sacar(self, valor):
        valor = self._validar_valor(valor)
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor
