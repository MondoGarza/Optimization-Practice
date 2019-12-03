#Find pairs in array which are k distance apart
#Create hash table for O(n) lookup of integers
def pairs(arr, k):
	hashT = set(arr) #Iterate over arr(O(n)) and place into set(O(1)) => O(n)
	ans = []
	for value in arr: #Iterate over arr(O(n)) and check set(O(1)) => O(n)
		if (value + k) in hashT:
			ans.append((value, value+k))

	#Total Complexity => O(n+n) => O(2n) => O(n)
	return ans

#Example arr and k
arr = [1,7,5,9,2,12,3]
k = 2
print(pairs(arr, k))