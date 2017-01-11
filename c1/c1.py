def isDivisibleBy3(n):
	if (n % 3 == 0):
		res = 1
	else:
		res = 0

	return res

def isDivisibleBy5(n):
	if (n % 5 == 0):
		res = 1
	else:
		res = 0

	return res

sum = 0
for number in range(1000):
	if (isDivisibleBy3(number) or isDivisibleBy5(number)):
		sum += number

print sum