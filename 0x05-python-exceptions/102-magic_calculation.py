#!/usr/bin/python3
def magic_calculation(a, b):
    temp = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                temp += a ** b / x
        except Exception as e:
            temp = b + a
            break
    return (temp)
