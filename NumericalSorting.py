import heapq

def sortGivenMovements(array, moves):
	theHeap = array[0:4]
	heapq.heapify(theHeap)
	sortedArray = []

	readIndex = moves + 1
	while readIndex < len(array):
		sortedArray.append(heapq.heappop(theHeap))
		if array[readIndex] < theHeap[0]:
			heapq.heapreplace(array[readIndex])
			readIndex += 1
			continue
		heapq.heappush(theHeap, array[readIndex])

	while not theHeap.isEmpty():
		sortedArray.append(heapq.heappop(theHeap))

	return sortedArray

theArray = [6,5,3,2,8,10,9]
moves = 3

print(sortGivenMovements(theArray,moves))