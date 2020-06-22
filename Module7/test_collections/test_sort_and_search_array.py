import unittest
import array as arr
from fun_with_collections import sort_and_search_array


class TestList(unittest.TestCase):
    def setUp(self):
        self.initial_list = arr.array('i', [4, 10, 7])
        self.expected = arr.array('i', [4, 7, 10])

    def test_item_sorted(self):
        sort_and_search_array.sort_array(self.initial_list)
        self.assertTrue(self.initial_list, self.expected)

    def test_item_search_good(self):
        result = sort_and_search_array.search_array(self.initial_list, 10)
        self.assertTrue(result, 1)

    def test_item_search_bad(self):
        result = sort_and_search_array.search_array(self.initial_list, 11)
        self.assertTrue(result, -1)


if __name__ == '__main__':
    unittest.main()
