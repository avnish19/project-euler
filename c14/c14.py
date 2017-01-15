"""
Module to provide solution to Challenge 14
"""
import sys
import math


def next_collatz_seq(current_number):
    """Returns the next collatz sequence number after current_number"""
    next_number = 0
    if current_number == 1:
        next_number = 0
    elif current_number % 2 == 0:
        next_number = current_number / 2
    else:
        next_number = (current_number * 3) + 1

    return next_number

longest_chain = 0
longest_start_num = 0

for starting_number in range(1000000, 1, -1):
    chain_length = 0
    chain_number = starting_number
    
    while chain_number >= 1:
        chain_length += 1
        chain_number = next_collatz_seq(chain_number)

    if chain_length > longest_chain:
        longest_chain = chain_length
        longest_start_num = starting_number

print longest_start_num, longest_chain