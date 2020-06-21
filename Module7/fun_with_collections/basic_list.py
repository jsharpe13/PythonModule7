"""
Program: basic_list.py
Author: Jacob Sharpe
Last date modified: 6/21/2020

The purpose of this program is to ask for input and output a basic list
"""


def make_list():
    """ calls get_input three times and returns a basic list
       :return list of inputs
        """
    the_list = []
    for x in range(3):
        methodInput = int(get_input())
        the_list.append(methodInput)

    return the_list


def get_input():
    """ asks and checks for numeric input and returns the input cast to a string
        :return string of user input
            """
    isValid = False
    while not isValid:
        try:
            UserInput = int(input("Please enter a number"))
            isValid = True
        except ValueError:
            print("I'm sorry that does not work.")
    return str(UserInput)


if __name__ == '__main__':
    print(make_list())
