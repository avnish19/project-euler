def palindrome(input):
    length = len(input)
    for i in range(length/2):
        if (input[i] != input[length-i-1]):
            return False
    return True

top = [0,0,0]

for x in range(999, 0, -1):
    for y in range(999, 0, -1):
        prod = x * y
        if (palindrome(str(prod))):
            if (prod > top[0]):
                top[0] = prod
                top[1] = x
                top[2] = y

print top[0], top[1], top[2]