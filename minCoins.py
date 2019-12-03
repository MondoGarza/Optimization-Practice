#returns minimum amount of coins needed to sum up to cost
#time complexity O(4) given coins list so => O(1)
def min_coins(cost):
	if cost < 1:
		return 1
	coins = [25,10,5,1]
	numCoins = 0
	for coin in coins:
		numCoins += cost // coin
		cost = cost % coin
		if cost == 0:
			break
	return numCoins

cost = 40
print(min_coins(cost))