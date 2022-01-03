#!/usr/bin/python3
def no_c(my_string):
    p = ""
    char1 = "c"
    char2 = "C"
    for i in my_string:
        if i == char1 or i == char2:
            continue
        p = p + i
    return (p)
