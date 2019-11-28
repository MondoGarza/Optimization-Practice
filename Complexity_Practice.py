import time
## Time complexity => 0(n)
## Space complexity => 0(1)
def foo(theList):
	theSum = 0
	product = 1
	for i in range(len(theList)):
		sum += theList[i]

	for i in range(len(theList)):
		product += theList[i]

	print(str(theSum) + "," + str(product))

## Time complexity => 0(n^2)
## Space complexity => 0(1)
def foo(theList):
	for i in range(len(theList)):
		for f in range(len(theList)):
			print(str(i) + "," + str(f))

## Time complexity => 0(n^2)
## Space complexity => 0(1)
def printUnorderedPairs(array):
	for i in range(len(array)):
		for j in range(len(array)):
			print(array[i] + "," + array[j])

## function for finding max fibonacci number
def fib(n):
	array = {}
	if n >= 0:
		array[0] = 0
	if n >= 1:
		array[1] = 1
	for i in range(2,n + 2):
		value = array[i-2] + array[i-1]
		if value > n:
			return list(array.values())
		else:
			array[i] = value

# (Public) Returns F(n).
#Time complexity = O(log(n))
#Space complexity = O(1)
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

n = 3053000
start = time.process_time()
fib(n)
finish = time.process_time()
print(finish-start)

start = time.process_time()
fibonacci(n)
finish = time.process_time()
print(finish-start)

