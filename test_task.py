import unittest
from task import sum_two_mins

class TaskTestCase(unittest.TestCase):

    def test_normal_array(self):
        arr = [4, 0, 3, 19, 492, -10, 1]
        result = sum_two_mins(arr)
        self.assertEqual(result, -10)

    def test_empty_array(self):
        arr = []
        self.assertRaises(ValueError, sum_two_mins, arr)

    def test_words_array(self):
        arr = ['foo', 'bar', 42]
        self.assertRaises(TypeError, sum_two_mins, arr)

    def test_array_1(self):
        arr = [-2,-3]
        result = sum_two_mins(arr)
        self.assertEqual(result, -5)

    def test_array_2(self):
        arr = [-2]
        self.assertRaises(ValueError, sum_two_mins, arr)

    def test_array_3(self):
        arr = [i for i in range(1000)]
        result = sum_two_mins(arr)
        self.assertEqual(result, 1)

    def test_array_4(self):
        arr = [i for i in range(-500000, 500000)]
        result = sum_two_mins(arr)
        self.assertEqual(result, -999999)

if __name__ == '__main__':
    unittest.main()
