
import pytest
from src.conta_bancaria import ContaBancaria

def test_saldo_inicial_zero():
    conta = ContaBancaria()
    assert conta.saldo == 0

def test_deposito_aumenta_saldo():
    conta = ContaBancaria()
    conta.depositar(100)
    assert conta.saldo == 100

def test_deposito_valor_invalido():
    conta = ContaBancaria()
    import pytest
    with pytest.raises(ValueError):
        conta.depositar(0)
    with pytest.raises(ValueError):
        conta.depositar(-10)

def test_saque_diminui_saldo():
    conta = ContaBancaria()
    conta.depositar(200)
    conta.sacar(50)
    assert conta.saldo == 150

def test_saque_maior_que_saldo():
    conta = ContaBancaria()
    conta.depositar(100)
    import pytest
    with pytest.raises(ValueError):
        conta.sacar(200)

def test_valores_nao_numericos_rejeitados():
    conta = ContaBancaria()
    import pytest
    with pytest.raises(TypeError):
        conta.depositar('100')
    with pytest.raises(TypeError):
        conta.sacar('50')
    with pytest.raises(TypeError):
        conta.depositar(None)
