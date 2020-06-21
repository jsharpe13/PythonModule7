def make_list():
    the_list = []
    for x in range(3):
        methodInput = int(get_input())
        the_list.append(methodInput)

    return the_list


def get_input():
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
