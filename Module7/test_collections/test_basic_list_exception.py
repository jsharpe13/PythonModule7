import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='7')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [7, 7, 7])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='0')  # patch function for input
    def test_make_list_below_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='51')  # patch function for input
    def test_make_list_above_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()



if __name__ == '__main__':
    unittest.main()