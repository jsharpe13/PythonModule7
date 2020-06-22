"""
Program: File_IO.py
Author: Jacob Sharpe
Last date modified: 6/21/2020

takes input to print them out to a text file
"""


def write_to_file(tur):
    """ writes the tuple to the txt file
    :param tuple to be written to the txt file
        """
    with open('student_info.txt', 'a') as f:
        f.write("\n")
        for x in tur:
            f.write(x + " ")
    f.close()


def get_student_info(**kwargs):
    """ gets input to print to the txt file
        :param keyword argument that is the student name
        """
    sentinel_Value = 'exit'
    isgoing = True
    temp = []
    for key, value in kwargs.items():
        temp.append("%s = %s" % (key, value))

    while isgoing:
        userInput = input("Enter a score: ")
        if userInput == sentinel_Value:
            isgoing = False
        else:
            temp.append(userInput)

    finalTuple = tuple(temp)
    write_to_file(finalTuple)


def read_to_file():
    """ reads the txt file and prints it to the console
    """
    f = open('student_info.txt', 'r')
    line = f.read()
    print(line)


if __name__ == '__main__':
    get_student_info(name="Jacob")
    get_student_info(name="John")
    get_student_info(name="Jack")
    get_student_info(name="Joe")
    read_to_file()
    end = input('Press any key to end')
    print('end')
