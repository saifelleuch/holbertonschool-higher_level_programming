#!/usr/bin/python3
""" inheritance tasks """


def inherits_from(obj, a_class):
    """ Only sub class of """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
