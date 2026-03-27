import unittest

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


class OperationTests(unittest.TestCase):
    def test_add(self):
        cases = [
            (2, 5, 7),
            (2.3, 6.7, 9),
            ('hello', 6, TypeError)
        ]

        for a, b, expected in cases:
            if isinstance(expected, type) and issubclass(expected, Exception):
                with self.assertRaises(expected):
                    add(a, b)

            else:
                self.assertEqual(add(a, b), expected)

    def test_subtract(self):
        cases = [
            (6, 2, 4),
            (4, 7, -3),
            (5.5, 1, 4.5),
            ('hello', 4, TypeError)
        ]

        for a, b, expected in cases:
            if isinstance(expected, type) and issubclass(expected, Exception):
                with self.assertRaises(expected):
                    subtract(a, b)
            else:
                self.assertEqual(subtract(a, b), expected)

    def test_multiply(self):
        cases = [
            (2, 3, 6),
            (1.5, 2, 3),
            ('hello', 5, TypeError)
        ]

        for a, b, expected in cases:
            if isinstance(expected, type) and issubclass(expected, Exception):
                with self.assertRaises(expected):
                    multiply(a, b)
            else:
                self.assertEqual(multiply(a, b), expected)

    def test_divide(self):
        cases = [
            (9, 3, 3),
            (10, 0.5, 20),
            (4, 0, ZeroDivisionError),
            ('hello', 3, TypeError)
        ]

        for a, b, expected in cases:
            if isinstance(expected, type) and issubclass(expected, Exception):
                with self.assertRaises(expected):
                    divide(a, b)
            else:
                self.assertEqual(divide(a, b), expected)
