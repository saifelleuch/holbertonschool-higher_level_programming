#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary_items = list(a_dictionary.items())
    for i, j in sorted(dictionary_items):
        print(i, ": ", j, sep="")
