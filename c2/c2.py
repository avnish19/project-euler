def fib(n):
  def fib_help(a, b, n):
    return fib_help(b, a+b, n-1) if n > 0 else a
  return fib_help(0, 1, n)

def isEven(n):
	if (n % 2 == 0):
		return 1
	return 0

n = 1
nthFib = 1
sum = 1
while (nthFib < 4000000):
	n += 1
	nthFib = fib(n)
	if isEven(nthFib):
		sum += nthFib

for i in range(10):
	print fib(i)

print sum