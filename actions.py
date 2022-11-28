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
	return sorted(indices.items(), key = lambda item : len(item[1]), reverse=True)

def score(grid):
     unique, counts = np.unique(grid, return_counts=True)
     if len(unique)==1:
         return 100000
     else:
         return int(max(counts)-min(counts))

def split(grid):
	largest_rectangle = getIndices(grid)[0][1]
	new_num = len(np.unique(grid))+1
	# make this more elegant
	dimensions = [largest_rectangle[-1][0]-largest_rectangle[0][0]+1, largest_rectangle[-1][1]-largest_rectangle[0][1]+1]
	tile_num = (max(dimensions)//2) * min(dimensions)

	if max(dimensions)%2==0:
		tile_num = tile_num - min(dimensions)

	n = tile_num/dimensions[0]
	if (math.floor(n)==n):
		index = []
		take = int(tile_num/dimensions[0])
		skip = int(dimensions[1]-n)
		for i in range(take):
			index = index + largest_rectangle[i:len(largest_rectangle):skip+take]
		for i in range(len(index)):
			grid[index[i][0], index[i][1]] = new_num
	else:
		for i in range(tile_num):
			try:
				index = largest_rectangle[i]
				grid[index[0], index[1]] = new_num
			except:
				#maybe delete this before submtting
				print("SHIT")

	return [grid]


def merge(grid):
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
				# check point is a point in the grid and is not the smallest rectangle itself
				merge_options.append(index)

	choice = random.choice(merge_options)

	numbers = []
	grids = []

	for c in merge_options:
		numbers.append(grid[c[0], c[1]])
	numbers = set(numbers)

	for n in numbers:
		for i in smallest_rectangle:
			grid[i[0], i[1]] = n

		g = copy.copy(grid)
		grids.append(g)

	return grids


def initialiseGrid(n):
    if n % 2 == 0:
        return np.ones((n, n))
    else:
        rows = []
        for j in range(n):
            for i in range(n//2):
                rows.append(1)
            for i in range(n-(n//2)):
                rows.append(2)
        grid = np.asarray(rows)
        return grid.reshape(n, n)

if __name__ == '__main__':
	t=[]
	grid = initialiseGrid(12)
	for i in range(4):
		print(split(grid))
		print(score(grid))
		print(isValid(grid))
	print("\nMERGING OPTIONS\n")
	grids = merge(grid)
	for g in grids:


		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

		if (isValid(g)):
			print("A valid merge option")
			print(g)
			print(isValid(g))
			print(score(g))
