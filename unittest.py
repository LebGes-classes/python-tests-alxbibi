import pytest

def add(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    return a + b


def subtract(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    return a - b


def multiply(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    return a * b


def divide(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError

    if b == 0:
        raise ZeroDivisionError

    return a / b

@pytest.mark.parametrize('a, b, expected', [
    (2, 5, 7),
    (2.3, 6.7, 9),
    ('hello', 6, TypeError)
])
def test_add(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            add(a, b)
    else:
        assert add(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (6, 2, 4),
    (4, 7, -3),
    (5.5, 1, 4.5),
    ('hello', 4, TypeError)
])
def test_subtract(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            subtract(a, b)
    else:
        assert subtract(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 6),
    (1.5, 2, 3),
    ('hello', 5, TypeError)
])
def test_multiply(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            multiply(a, b)
    else:
        assert multiply(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (9, 3, 3),
    (10, 0.5, 20),
    (4, 0, ZeroDivisionError),
    ('hello', 3, TypeError)
])
def test_divide(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            divide(a, b)
    else:
        assert divide(a, b) == expected
