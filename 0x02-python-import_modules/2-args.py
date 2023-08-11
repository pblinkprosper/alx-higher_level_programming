#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1
    print(f"{arg} {'argument' if arg == 1 else 'arguments'}", end="")
    print(f"{'.' if arg == 0 else ':'}")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
