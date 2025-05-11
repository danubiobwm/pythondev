import pytest
from functions import encontrar_valor, somar_lista

def test_somar_lista():
    # Testa a soma de uma lista de números
    assert somar_lista([1, 2, 3]) == 6
    assert somar_lista([-1, -2, -3]) == -6
    assert somar_lista([0, 0, 0]) == 0
    assert somar_lista([1.5, 2.5, 3.5]) == 7.5

    # Testa se levanta um erro quando a lista contém elementos não numéricos
    with pytest.raises(ValueError):
        somar_lista([1, 'a', 3])

def test_encontrar_valor():
    # Testa a busca de um valor em um dicionário
    dicionario = {'a': 1, 'b': 2, 'c': 3}
    assert encontrar_valor(dicionario, 'a') == 1
    assert encontrar_valor(dicionario, 'b') == 2
    assert encontrar_valor(dicionario, 'c') == 3
    assert encontrar_valor(dicionario, 'd') is None

    # Testa se levanta um erro quando o primeiro argumento não é um dicionário
    with pytest.raises(ValueError):
        encontrar_valor('não é um dicionário', 'a')