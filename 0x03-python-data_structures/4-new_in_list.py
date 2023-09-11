#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        fct_list = []
        for i in my_list:
                fct_list.append(i)
        fct_list[idx] = element
        return (fct_list)
