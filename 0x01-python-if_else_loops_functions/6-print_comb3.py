#!/usr/bin/python3
for i in range(0, 100):
    a = i // 10
    b = i % 10
    if a < b and a != b and i != 89:
        print("{:d}{:d}, ".format(a, b), end="")
print("89")
