#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list_of_integersst of unsorted integers"""
    list_length = len(list_of_integers)
    if list_length == 0:
        return
    middel = list_length // 2
    if (middel == list_length - 1 or list_of_integers[middel] >= list_of_integers[middel + 1]) and (middel == 0 or list_of_integers[middel] >= list_of_integers[middel - 1]):
        return list_of_integers[middel]
    if middel != list_length - 1 and list_of_integers[middel + 1] > list_of_integers[middel]:
        return find_peak(list_of_integers[middel + 1:])
    return find_peak(list_of_integers[:middel])