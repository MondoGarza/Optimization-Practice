#find 2 values which sum up to the target value
#No duplicates in arr
def sumto(arr,target):
	aSet = {}
	for val in arr:
		aSet[val] = False

	pairs = []
	for value in arr:
		compliment = target - value
		if compliment in aSet and compliment != value and aSet[value] != True:
			aSet[value] = True
			aSet[compliment] = True
			pairs.append([value, compliment])
	if not pairs:
		return "No valid pairs"
	return pairs

arr = [14,13,6,7,8,10,1,2]
target = 14
for pairs in sumto(arr,target):
	print(str(pairs[0])+" and "+str(pairs[1]))
