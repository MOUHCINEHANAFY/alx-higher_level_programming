#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        cnt += 1
        try:
            print("{}".format(my_list[i]), end="")
        except:
            cnt -= 1
    print()
    return (cnt)
