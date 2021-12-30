#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
            print("1:", argv[1])
        else:
            print(len(argv) - 1, "arguments:")
            for n, argv in enumerate(argv[1:]):
                print(n + 1, ":", sep="", end=" ")
                print(argv)
