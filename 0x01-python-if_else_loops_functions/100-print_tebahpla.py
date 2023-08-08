#!/usr/bin/python3
for abc in reversed(range(97, 123)):
    print("{:c}".format(abc if (abc % 2 == 0) else (abc - 32)), end='')
