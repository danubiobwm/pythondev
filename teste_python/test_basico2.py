
from functions import length, sub, validateEmail

def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 5) == 5
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0
    assert sub(-1, 1) == -2

def test_length():
    assert length([1, 2, 3]) == 3
    assert length([]) == 0
    assert length([1, 2, 3, 4, 5]) == 5
    assert length([1]) == 1
    assert length([1, 2]) == 2

def test_validateEmail():
    assert validateEmail("jo@bol.com.br") is True
    assert validateEmail("jo@bol") is False
