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
		for j in range(1:len(array)$):
			print(array[i] + "," + array[j])




