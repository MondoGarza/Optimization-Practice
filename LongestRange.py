#Time Complexity => O(array) => O(n)
#Space Complexity => O(hashTable + answer) => O(n)
def longestRange(array):
	#Initialize the hashTable for number lookup as well as the longestLength variable
	hashTable= {}
	answer = []
	longestLength = 0

	#Iterate through the array and turn the array into a set
	for value in array:
		hashTable[value] = True

	#Iterate through the array
	for num in array:

		# Checks if value has been checked if, if so go to the next value in array else go ahead
		if not hashTable:
			continue

		# Check off that the value has been checked, intialize currentLength variable, rightValue, and Left
		hashTable[num] = True
		currentLength = 0
		rightValue = num + 1
		leftValue = num - 1

		# Checks for left values
		while leftValue in hashTable:
			hashTable[leftValue] = False
			currentLength += 1
			leftValue -= 1

		# Checks for right values
		while rightValue in hashTable:
			hashTable[rightValue] = True
			currentLength += 1
			rightValue += 1

		# Checks if the current length is bigger than the longest length
		if currentLength > longestLength:
			answer = [leftValue+1, rightValue-1]

	return answer


allow = [1,11,3,0,15,5,2,4,10,7,12,6]
print(longestRange(allow))



