#!/usr/bin/python3
"""A function that reads text file and prints to stdout"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
        f.close()
