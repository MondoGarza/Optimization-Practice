def riverSizes(matrix):
	rivers = []
	visited = [[False for values in row] for row in matrix]
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			if visited[row][column]:
				continue
			checkUncheckedRivers(row, column, matrix, visited, rivers)
	rivers = sorted(rivers)
	return rivers

def checkUncheckedRivers(row, column, matrix, visited, rivers):
	currentRiverCount = 0
	nodesToExplore = [[row, column]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		row = currentNode[0]
		column = currentNode[1]
		if visited[row][column]:
			continue
		visited[row][column] = True
		if matrix[row][column] == 0:
			continue
		currentRiverCount += 1
		unvisitedNeighbors = getUnvisitedNeighbors(row, column, matrix, visited)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverCount > 0:
		rivers.append(currentRiverCount)

def getUnvisitedNeighbors(row,column,matrix,visited):
	unvisitedNeighbors = []
	if row > 0 and not visited[row - 1][column]:
		unvisitedNeighbors.append([row - 1,column])

	if row < len(matrix) - 1 and not visited[row+1][column]:
		unvisitedNeighbors.append([row + 1,column])

	if column > 0 and not visited[row][column - 1]:
		unvisitedNeighbors.append([row,column - 1])

	if column < len(matrix[0]) - 1 and not visited[row][column + 1]:
		unvisitedNeighbors.append([row,column + 1])	
	return unvisitedNeighbors

theMatrix = [[0,0,1,1],[1,1,1,0],[1,1,1,0],[0,0,0,1]]
print(riverSizes(theMatrix))








