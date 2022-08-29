import unittest
import bubblesort as bs

class TestBubbleSort(unittest.TestCase):
    
    def test_bubblesort(self):
        self.assertEqual(bs.bubblesort([3, 7, 1, 9, 5]), [1, 3, 5, 7, 9])
    def test_bubblesort_one_number(self):
            self.assertEqual(bs.bubblesort([1]), [1])
    def test_bubblesort_without_numbers(self):
            self.assertEqual(bs.bubblesort([]), [])

if __name__ == '__name__':
    unittest.main()