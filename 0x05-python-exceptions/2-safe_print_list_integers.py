#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            if str(my_list[i]).isdigit():
                cnt += 1
            print("{:d}".format(my_list[i]), end='')
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return (cnt)
