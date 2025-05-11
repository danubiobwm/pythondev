import pytest

def function_unidade(x):
    """
    Função que retorna o quadrado de um número.
    """
    return x * 2

def function_integracao(x):
    """
    Função que retorna o quadrado de um número.
    """
    return x + 10

@pytest.mark.unit
def test_function_unidade():
    """
    Teste unitário para a função function_unidade.
    """
    assert function_unidade(2) == 4
    assert function_unidade(3) == 6
    assert function_unidade(0) == 0
    assert function_unidade(-1) == -2

@pytest.mark.integration
def test_function_integracao():
    """
    Teste de integração para a função function_integracao.
    """
    assert function_integracao(2) == 12
    assert function_integracao(3) == 13
    assert function_integracao(0) == 10
    assert function_integracao(-1) == 9

@pytest.mark.slow
def test_function_slow():
    """
    Teste lento para a função function_unidade.
    """
    import time
    time.sleep(2)

    assert function_unidade(1000000) == 2000000
    assert function_unidade(10000000) == 20000000
    assert function_unidade(0) == 0
    assert function_unidade(-1) == -2

