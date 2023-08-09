#!/usr/bin/python3
def remove_char_at(str, n):
    a = 0
    n_str = ""
    for ch in str:
        if a == n:
            n_str = n_str + ''
        else:
            n_str = n_str + ch
        a = a + 1
    return n_str
