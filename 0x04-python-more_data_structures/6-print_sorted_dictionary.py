#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for orderedky in sorted(a_dictionary.keys()):
        print("{}: {}".format(orderedky, a_dictionary[orderedky]))
