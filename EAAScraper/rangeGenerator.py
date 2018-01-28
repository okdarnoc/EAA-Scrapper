#!/usr/bin/env python3

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

"""
By default the function only loops over the alphabet C for the sake of demo
"""
def range_generator(start='C', end='C'):
    try:
        partition_size = ord(end) - ord(start) + 1
        if (partition_size <= 0):
            raise ValueError("In def range_generator(start, end) end must not be less than start")

        for i in range(partition_size):
            leading_alpha = chr(ord(start) + i)
            for j in range(999999):
                num = '{val:06d}'.format(val=j)
                yield leading_alpha +'-'+ num

    except TypeError:
        print("def range_generator(start, end) takes two capitalized alphabets as input")

if __name__ == "__main__":
    g = range_generator('A','B')
    for i in g:
        print(i)
    