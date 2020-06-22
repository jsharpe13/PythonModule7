"""
Program: sort_and_search_array.py
Author: Jacob Sharpe
Last date modified: 6/21/2020

sorts and search arrays for specific items
"""

import array as arr


def sort_array(array):
    """ sorts an array passed into it
        :param the array to be sorted
        """
    temp = array.tolist()
    temp.sort()
    a2 = arr.array('i', temp)
    return a2


def search_array(array, value):
    """ searches for an item in the array
     :param the array to be searched
     :param the value being searched for
     """
    Length = len(array.tolist())
    for i in range(Length):
        if array[i] == value:
            return i
    return -1


if __name__ == '__main__':
    a = arr.array('i', [4, 10, 7])
    result = sort_array(a)
    for x in result:
        print(x, end=' ')
    print("\nPosition:", search_array(a, 11))
