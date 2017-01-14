import sys

def triangle_number(n):
    """Returns the nth triangular number"""
    res = 0
    for num in range (1, n+1):
        res += num

    return res

def number_of_divisors(n):
    """Returns the number of divisors of n"""
    res = 1

    for num in range (1, int(n+1/2)):
        if n % num == 0:
            res += 1
    
    return res

#test functions above
# print "tri_num\t", "|", "num_div" 
# for index in range(1, 11):
#     print str(triangle_number(index)) + "\t", ":", number_of_divisors(triangle_number(index))

largest_tri_num = 0
largest_num_of_divisors = 0
index = 1


while largest_num_of_divisors <= int(sys.argv[1]):
    # print "----- largest_num_of_divisors:", largest_num_of_divisors

    tri_num = triangle_number(index)
    num_div = number_of_divisors(tri_num)
    # print "index, tri_num, num_div:", index, tri_num, num_div

    if num_div > largest_num_of_divisors:
        largest_num_of_divisors = num_div
        largest_tri_num = tri_num
        # print "New largest_num_of_divisors found: ", largest_num_of_divisors, "for tri_num", tri_num

    index += 1

print "index:", index, "largest_tri_num:", largest_tri_num, ", largest_num_of_divisors:", largest_num_of_divisors