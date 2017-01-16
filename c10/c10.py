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

USER_INPUT = int(sys.argv[1])

sum_of_primes = 0

for num in range(2, USER_INPUT+1, +1):
    if isPrime(num):
        sum_of_primes += num

print sum_of_primes