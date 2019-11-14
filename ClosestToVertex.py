#magnitude => sqrt(x^2+y^2)
import math

def closestToVertex(pList, vertex):
	smallestDistance = (float('inf'))
	smallestPoint = []
	for point in pList:
		currentDistance = math.sqrt((point[0] - vertex[0])**2 + (point[1] - vertex[1])**2)
		if currentDistance < smallestDistance:
			smallestDistance = currentDistance
			smallestPoint = point
	return smallestPoint

vertex = [0,0]
points = [[2,5],[10,10],[3,10],[1,1],[0,1]]

print(closestToVertex(points,vertex))

