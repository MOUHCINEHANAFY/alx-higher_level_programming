#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    names = []
    for i in dir(hidden_4):
        if i[0] != '_':
            names.append(i)
    for i in names:
        print(i)
