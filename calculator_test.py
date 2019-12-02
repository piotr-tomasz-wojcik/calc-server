import unittest
from calculator import calculate, InvalidEquation


class CalculatorTest(unittest.TestCase):
    def test_plusOperation(self):
        self.assertEqual(3, calculate(['+', [1, 2]]))
        self.assertEqual(-1, calculate(['+', [1, -2]]))

    def test_minusOperation(self):
        self.assertEqual(7, calculate(['-', [-1, -8]]))
        self.assertEqual(-5, calculate(['-', [1, 6]]))

    def test_multiplyOperation(self):
        self.assertEqual(9, calculate(['*', [3, 3]]))
        self.assertEqual(-15, calculate(['*', [3, -5]]))

    def test_divideOperation(self):
        self.assertEqual(3, calculate(['/', [9, 3]]))
        self.assertEqual(5, calculate(['/', [15, 3]]))

    def test_invalidOperation(self):
        self.assertRaises(InvalidEquation, calculate, ['/', [9, 0]])
        self.assertRaises(InvalidEquation, calculate, ['\\', [9, 5]])
        self.assertRaises(InvalidEquation, calculate, ['+', ['a', 5]])
        self.assertRaises(InvalidEquation, calculate, ['-', [9, 'b']])
        self.assertRaises(InvalidEquation, calculate, ['z', [9, 3]])
        self.assertRaises(InvalidEquation, calculate, ['+'])
        self.assertRaises(InvalidEquation, calculate, None)
        self.assertRaises(InvalidEquation, calculate, [])
        self.assertRaises(InvalidEquation, calculate, ['+', [3]])
        self.assertRaises(InvalidEquation, calculate, ['+', []])
        self.assertRaises(InvalidEquation, calculate, ['+', 3])
        self.assertRaises(InvalidEquation, calculate, ['+', [2, 3, 4]])
        self.assertRaises(InvalidEquation, calculate, [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
