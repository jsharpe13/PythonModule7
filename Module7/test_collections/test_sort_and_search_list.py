import unittest
from fun_with_collections import sort_and_search_list


class TestList(unittest.TestCase):
    def setUp(self):
        self.initial_list = [4, 10, 3]
        self.expected = [3, 4, 10]

    def test_item_sorted(self):
        sort_and_search_list.sort_list(self.initial_list)
        self.assertTrue(self.initial_list == self.expected)

    def test_value_found(self):
        value = 10
        result = sort_and_search_list.search_list(self.initial_list, value)
        self.assertTrue(result)

    def test_value_not_found(self):
        value = 15
        result = sort_and_search_list.search_list(self.initial_list, value)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
