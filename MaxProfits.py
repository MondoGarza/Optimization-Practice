## unoptimized solution
## optimized solution
## Time => O(kn^2)
## Space => O(nk)
def maxProfitUnOptimized(prices, k):
	n = len(prices)

	if not len(prices):
		return 0

	profit = [[0 for i in range(k+1)] for j in range(n)]

	for t in range(1, k+1):
		maxThusFar = float("-inf")

	for i in range(1,n):
		for j in range(1,k+1):
			max_so_far = 0
			for l in range(i):
				max_so_far = max(max_so_far, prices[i] - prices[l] + profit[l][j-1])
			profit[i][j] = max(profit[i - 1][j], max_so_far)

	return profit[n-1][k]

## optimized solution
## Time => O(kn)
## Space => O(nk)
def maxProfitOptimizedSpace(prices, k):
	n = len(prices)
	profit = [[0 for i in range(n + 1)] for j in range(k+1)]

	for i in range(1,k + 1):
		prevDiff = float('-inf')

		for j in range(1,n):
			prevDiff = max(prevDiff, profit[i - 1][j - 1] - prices[j-1])
			profit[i][j] = max(profit[i][j-1], prices[j] + prevDiff)
	return profit[k][n-1]

## optimized solution
## Time => O(kn)
## Space => O(n)
def maxProfitOptimizedNoSpace(prices, k):
	if not len(prices):
		return 0

	evenProfits = [0 for d in prices]
	oddProfits = [0 for d in prices]

	for t in range(1, k + 1):
		maxThusFar = float('-inf')
		if t % 2 == 1:
			currentProfits = oddProfits
			previousProfits = evenProfits
		else:
			currentProfits = evenProfits
			previousProfits = oddProfits
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d-1])
			currentProfits[d] = max(currentProfits[d-1], maxThusFar + prices[d])
	return evenProfits[-1] if k % 2 else oddProfits[-1]

k = 2
prices = [5,11,3,50,60,90]
print(maxProfitUnOptimized(prices,k))
print(maxProfitOptimizedSpace(prices,k))
print(maxProfitOptimizedNoSpace(prices,k))