import unittest
import equation

class TestEquation(unittest.TestCase):
    def test_equation_two_roots(self):
        self.assertEqual(equation.getRoots(1, 8, -9), [1.0, -9])

    def test_equation_one_root(self):
        self.assertEqual(equation.getRoots(9, -12, 4), [2/3])
        
    def test_equation_without_roots(self):
        self.assertEqual(equation.getRoots(5, 4, 9), [])

if __name__ == '__name__':
    unittest.Equation()