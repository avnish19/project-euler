"""
Module to provide solution to Challenge 12
"""
import sys
import math


def triangle_number(nth):
    """Returns the nth triangular number"""
    return nth * (nth + 1) / 2


def number_of_divisors(input_number):
    """Returns the number of divisors of input_number"""
    res = 0

    # check for square root divisor
    if math.sqrt(input_number) % 1 == 0:
        res += 1

    # check for other integer divisors
    for num in range(1, int(math.ceil(math.sqrt(input_number)))):
        if input_number % num == 0:
            res += 2

    return res

# test functions above
print "index\t", "|", "tri_num\t", "|", "num_div"
for index in range(1, 11):
    print str(index) + "\t", ":", str(triangle_number(index)) + "\t\t", ":", number_of_divisors(triangle_number(index))

largest_tri_num = 0
largest_num_of_divisors = 0
index = 1

print number_of_divisors(45)

while largest_num_of_divisors <= int(sys.argv[1]):
    # print "----- largest_num_of_divisors:", largest_num_of_divisors

    tri_num = triangle_number(index)
    num_div = number_of_divisors(tri_num)
    # print "index, tri_num, num_div:", index, tri_num, num_div

    if num_div > largest_num_of_divisors:
        largest_num_of_divisors = num_div
        largest_tri_num = tri_num
        # print "New largest_num_of_divisors found: ", largest_num_of_divisors,
        # "for tri_num", tri_num

    index += 1

print "index:", index, "largest_tri_num:", largest_tri_num, ", largest_num_of_divisors:", largest_num_of_divisors
