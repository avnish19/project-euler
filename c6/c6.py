#!/usr/bin/python
import sys

def expand(n, r):
    total = 0
    for i in range(n+1, r+1, +1):
        total += 2*n*i

    return total

limit = int(sys.argv[1])
total = 0
for i in range(1, limit+1, +1):
    total += expand(i, limit)

print total