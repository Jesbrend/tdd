
import pytest
from src.conta_bancaria import ContaBancaria

def test_saldo_inicial_zero():
    conta = ContaBancaria()
    assert conta.saldo == 0
