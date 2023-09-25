#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        try:
            print("Inside result: {}".format(value))
        except TypeError:
            print("Inside result: {}".format(None))
            return (None)
    return (value)
