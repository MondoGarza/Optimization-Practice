import math

def vertexDist(points,vertex,k):
	closest_points = []
	distance = float('inf')
	y_vertex = vertex[1]
	x_vertex = vertex[0]
	for point in points:
		x_point = point[0]
		y_point = point[1]
		current_distance = math.sqrt((x_point-x_vertex)**2 + (y_point-y_vertex)**2)
		if current_distance < distance:
			distance = current_distance
			closest_points.append(point)
	return closest_points
			
points = [[1,2],[2,3],[1,-3]]
vertex = [2,2]
k = 2
print(vertexDist(points,vertex,k))