import pytest

def adicionar(a, b):
    """
    Função que soma dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma de a e b
    """
    return a + b


@pytest.mark.parametrize(
    "a, b, resultado",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (3.5, 2.5, 6.0)
    ]
)

def test_adicionar(a, b, resultado):
    """
    Testa a função adicionar com diferentes conjuntos de dados.
    :param a: Primeiro número
    :param b: Segundo número
    :param resultado: Resultado esperado
    """
    assert adicionar(a, b) == resultado


