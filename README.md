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
