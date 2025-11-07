# Sistema de Conta Bancária — TDD

Projeto desenvolvido com TDD (RED → GREEN → REFACTOR).

- Projeto escolhido: Sistema de Conta Bancária
- Ferramenta de teste: PyTest
- Linguagem: Python 3.10+

## Regras
- Conta inicia com saldo 0.
- Depósito: valor numérico > 0.
- Saque: valor numérico > 0 e <= saldo.
- Rejeita valores não numéricos (ex.: string, None).

## Como executar os testes
1. Crie e ative um ambiente virtual (Windows):

   python -m venv .venv
   .venv\\Scripts\\activate
   pip install pytest

2. Rode os testes:

   pytest

## Experiência com TDD
- Cada funcionalidade iniciou por um teste que falha (RED), depois implementei o mínimo para passar (GREEN) e refatorei mantendo todos os testes verdes (REFACTOR).
- O histórico de commits reflete essa evolução incremental.

## Histórico TDD

- 1) test: cria teste para saldo inicial zero (RED)
- 2) feat: implementa ContaBancaria com saldo inicial zero (GREEN)
- 3) test: adiciona teste para depósito válido (RED)
- 4) feat: implementa depósito simples (GREEN)
- 5) test: exige depósito > 0 (RED)
- 6) feat: valida depósito > 0 (GREEN)
- 7) test: adiciona teste para saque válido (RED)
- 8) feat: implementa saque simples (GREEN)
- 9) test: proíbe saque maior que saldo (RED)
- 10) feat: validações de saque (maior que zero e saldo suficiente) (GREEN)
- 11) test: rejeita valores não numéricos em depósito/saque (RED)
- 12) refactor: validação explícita de tipo numérico e método de validação; saldo em float (mantém testes verdes)

### Commits auxiliares
- chore: adiciona pyrightconfig para Pylance resolver imports de src
- chore: VS Code settings (extraPaths) e __init__ em src para Pylance
- chore: ajusta import para 'src.conta_bancaria' e remove hack de sys.path
