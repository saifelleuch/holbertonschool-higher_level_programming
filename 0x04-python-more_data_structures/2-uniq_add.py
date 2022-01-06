#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = 0
    for i in my_list:
        if my_list[i] != my_list[i + 1]:
            sum = sum + my_list[i]
        else:
            sum = sum + my_list[i + 1]
            continue
    return (sum)
