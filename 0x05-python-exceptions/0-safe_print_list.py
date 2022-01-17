#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(my_list[0], my_list[x]):
            print(i, end="")
    except IndexError:
        for i in my_list:
            print(i, end="")
    print("")
    for i in my_list:
        counter = counter + 1
    if x >= counter:
        return (counter)
    else:
        return (x)
