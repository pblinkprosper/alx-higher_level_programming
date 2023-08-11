#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    args = sys.argv
    for i in range(1, len(args)):
        total = total + int(args[i])
    print(total)
