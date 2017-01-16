import sys
import math

#!/usr/bin/python
def isPrime(n):
    """Check if input int n is prime"""
    sqrt_n = int(math.floor(math.sqrt(n)))
    res = True

    for div in range(2, sqrt_n+1, +1):
        if n % div == 0:
            res = False
            break

    return res

NTH_PRIME = int(sys.argv[1])
prime_count = 0
num = 2

while (prime_count < NTH_PRIME):
    if isPrime(num):
        prime_count += 1
        print num, "is the", prime_count, "th prime number"

    num += 1