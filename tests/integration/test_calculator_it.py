"""«Внутренние» тесты: запускаются только в GitLab, в GitHub Actions не вызываются."""

import unittest

from lab import Calculator


class CalculatorIT(unittest.TestCase):
    def test_chain_of_operations(self):
        calc = Calculator()
        result = calc.divide(calc.multiply(calc.add(2, 4), 3), 2)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
