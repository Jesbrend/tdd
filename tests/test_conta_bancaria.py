import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

import pytest
from conta_bancaria import ContaBancaria

def test_saldo_inicial_zero():
    conta = ContaBancaria()
    assert conta.saldo == 0
