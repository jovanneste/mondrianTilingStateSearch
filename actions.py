import numpy as np
from visualiseActions import *
from validateActions import *
import random
import math
import copy


def getIndices(grid):
	unique = np.unique(grid)
	indices = {}
	for n in unique:
		i = np.nonzero(grid==n)
		indexes = []
		for j in range(len(i[0])):
			indexes.append([i[0][j], i[1][j]])
		indices.update({n:indexes})
	return sorted(indices.items(), key=lambda item : len(item[1]), reverse=True)


def split(grid):
	grids = []
	index = []
	largest_rectangle = getIndices(grid)[0][1]
	new_num = len(np.unique(grid))+1
	dimensions = [largest_rectangle[-1][0]-largest_rectangle[0][0]+1, largest_rectangle[-1][1]-largest_rectangle[0][1]+1]
	tile_num = (max(dimensions)//2) * min(dimensions)

	if max(dimensions)%2==0:
		tile_num = tile_num - min(dimensions)

	n = tile_num/dimensions[0]

	if tile_num%dimensions[1]==0:
		# add horizontally
		for index in range(tile_num):
			x = largest_rectangle[index][0]
			y = largest_rectangle[index][1]
			grid[x, y] = new_num
	else:
		# add vertically
		take = int(tile_num/dimensions[0])
		skip = int(dimensions[1]-n)
		for i in range(take):
			index = index + largest_rectangle[i:len(largest_rectangle):skip+take]
		for i in index:
			x = i[0]
			y = i[1]
			grid[x,y] = new_num

	return [grid]


def merge(grid):
	grid = np.squeeze(grid)
	smallest_rectangle = getIndices(grid)[-1][1]
	surroundings = []
	merge_options = []
	for index in smallest_rectangle:
		surroundings.append([sum(i) for i in zip(index, [1,0])])
		surroundings.append([sum(i) for i in zip(index, [0,1])])
		surroundings.append([sum(i) for i in zip(index, [-1,0])])
		surroundings.append([sum(i) for i in zip(index, [0,-1])])

	for index in surroundings:
		if index not in smallest_rectangle:
			if grid.shape[0] not in index:
				if index[0]!=len(grid[0]) and index[1]!=len(grid[0]):
				# check point is a point in the grid and is not the smallest rectangle itself
					merge_options.append(index)

	numbers = []
	grids = []
	for c in merge_options:
		numbers.append(grid[c[0], c[1]])
	numbers = set(numbers)

	for n in numbers:
		for i in smallest_rectangle:
			grid[i[0], i[1]] = n

		g = copy.deepcopy(grid)
		grids.append(g)


	return grids
