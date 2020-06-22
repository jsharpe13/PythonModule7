"""
Program: average_score_assignment.py
Author: Jacob Sharpe
Last date modified: 6/21/2020

print out a series of abritary and keyword arguments
"""


def average_scores(*args, **kwargs):
    """ prints out the average from abritary and keyword arguments
           :param arbitary argument
           :param keyword arguments
            """
    sum = 0
    total = 0
    sumAverage = 0
    for arg in args:
        sum = sum + arg
        total = total + 1

    sumAverage = sum / total
    for key, value in kwargs.items():
        print("%s = %s" % (key, value), end=' ')
    print(sumAverage)


if __name__ == '__main__':
    print("Result:", end=' ')
    average_scores(57, 68, 82, 55, name='Michelle', gpa='2.0', course='Python with current average')
    print("Result:", end=' ')
    average_scores(100, 100, 99, 99, 98, name='Jacob', gpa='4.0', course='Computer Science with current average')
    print("Result:", end=' ')
    average_scores(15, 20, name='Jessica', gpa='1.0', course='French with current average')
