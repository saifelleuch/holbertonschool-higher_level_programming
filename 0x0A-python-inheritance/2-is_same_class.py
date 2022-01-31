#!/usr/bin/python3
""" inheritance tasks """


def is_same_class(obj, a_class):
    """ Exact same object task """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    else:
        return False
