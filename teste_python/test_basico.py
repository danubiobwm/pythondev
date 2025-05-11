
from functions import is_positive


def test_soma():
    assert sum([1, 2, 3]) == 6


def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(-1) == False
    assert is_positive(0) == False
    assert is_positive(3.14) == True
    assert is_positive(-2.5) == False