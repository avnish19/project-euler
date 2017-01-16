import sys
import math

#!/usr/bin/python

def is_pythagorean_triplet(a_num, b_num, c_num):
    """Checks if the 3 input digits (int) form a Pythagorean Triplet"""
    res = False
    if (a_num**2 + b_num**2) == c_num**2:
        res = True

    return res

for x in range(1, 333, +1):
    # raw_input("..")
    for y in range(x+1, int(math.ceil((1000-x+1)/2)), +1):
        z = 1000 - x - y
        # print x, y, z, "sums to", x+y+z
        if is_pythagorean_triplet(x, y, z):
            print "WIN:", x, y, z, "produces", x*y*z
