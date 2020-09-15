import pytest
from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido

@pytest.fixture
def usuario_bruno():
    return Usuario('bruno', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Video Game')

def test_deve_ter_saldo_na_carteira_quando_usuario_propor_lance(usuario_bruno, leilao):
    usuario_bruno.propoe_lance(leilao, 50.0)
    assert usuario_bruno.carteira >= 0

def test_deve_permitir_lance_quando_usuario_propor_valor_menor_que_a_carteira(usuario_bruno, leilao):
    usuario_bruno.propoe_lance(leilao, 1.0)
    assert usuario_bruno.carteira == 99.0

def test_deve_permitir_lance_quando_usuario_propor_valor_igual_a_carteira(usuario_bruno, leilao):
    usuario_bruno.propoe_lance(leilao, 100.0)
    assert usuario_bruno.carteira == 0

def test_nao_deve_permitir_lance_quando_usuario_propor_valor_maior_que_a_carteira(usuario_bruno, leilao):
    with pytest.raises(LanceInvalido):
        usuario_bruno.propoe_lance(leilao, 200.00)
