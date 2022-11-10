import numpy as np
from validateAction import isValid
from visualiseActions import *


def getIndices(grid):
	unique = np.unique(grid)
	indices = {}
	for n in unique:
		i = np.nonzero(grid==n)
		indexes = []
		for j in range(len(i[0])):
			indexes.append([i[0][j], i[1][j]])
		indices.update({n:indexes})
	return sorted(indices.items(), key = lambda item : len(item[1]), reverse=True)


# largest rectangle in square to try split 
# if area if odd - both sides must be odd 
def split(grid):
	largest_rectangle = getIndices(grid)[0][1]
	new_num = len(np.unique(grid))+1
	# make this more elegant 
	dimensions = [largest_rectangle[-1][0]-largest_rectangle[0][0]+1, largest_rectangle[-1][1]-largest_rectangle[0][1]+1]
	tile_num = (max(dimensions)//2) * min(dimensions)

	if max(dimensions)%2==0:
		tile_num = tile_num - min(dimensions)

	for i in range(tile_num):
		index = largest_rectangle[i]
		grid[index[0], index[1]] = new_num

	return grid 


t = np.array([[1,1,1,2,2],
     		[1,1,1,2,2],
     		[1,1,1,2,2],
     		[1,1,1,2,2],
     		[3,3,3,2,2]])


visualiseColours(t, 'test_bsplit')
t = split(t)
visualiseColours(t, 'test_asplit')