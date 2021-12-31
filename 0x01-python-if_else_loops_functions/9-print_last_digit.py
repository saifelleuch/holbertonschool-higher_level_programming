#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        C = number % 10
        print(C, end="")
        return(C)
    if number < 0:
        C = (number * -1) % 10
        print(C, end="")
        return(C)
