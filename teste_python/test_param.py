import pytest

def calcular_area(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    :param base: La longitud de la base del triángulo.
    :param altura: La altura del triángulo.
    :return: El área del triángulo.
    """
    return base * altura


@pytest.fixture
def datos_triangulo():
    """
    Fixture que proporciona los datos de un triángulo para las pruebas.
    """
    return [
      {"base": 5, "altura": 10, "area": 25},
      {"base": 3, "altura": 6, "area": 9},
      {"base": 7, "altura": 2, "area": 7},
      {"base": 0, "altura": 5, "area": 0},
    ]


@pytest.mark.parametrize("dados", [
    {"base": 5, "altura": 10, "area": 25},
    {"base": 3, "altura": 6, "area": 9},
    {"base": 7, "altura": 2, "area": 7},
    {"base": 0, "altura": 5, "area": 0},
])

def test_calcular_area(dados):
    """
    Prueba unitaria para la función calcular_area.

    :param triangulo: Un diccionario que contiene la base, altura y área esperada del triángulo.
    """
    base = dados["base"]
    altura = dados["altura"]
    area_esperada = dados["area"]

    area_calculada = calcular_area(base, altura)
