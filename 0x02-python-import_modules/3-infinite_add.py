#!/usr/bin/python3
from sys import argv
sum = 0
for i in argv[1:]:
    sum = sum + int(i)
print(sum)
