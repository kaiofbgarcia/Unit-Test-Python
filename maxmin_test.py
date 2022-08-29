import unittest
import maxmin

class TestMaxMin(unittest.TestCase):
    def test_maxmin(self):
        self.assertEqual(maxmin.MaxMin([10, 15, 20]), [20,10])

    def test_maximun(self):
        self.assertEqual(maxmin.Max([10, 100, 1000]), 1000)

    def test_minimun(self):
        self.assertEqual(maxmin.Min([10, 50, 100]), 10)

    def test_maxmin_two_numbers(self):
        self.assertEqual(maxmin.MaxMin([1, 1, 1, 1]), [1, 1])  

    def test_maxmin_with_one_number(self):
        self.assertEqual(maxmin.MaxMin([5]), [5,5])
  

if __name__ == '__name__':
    unittest.main()