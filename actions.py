import numpy as np
from validateAction import isValid

test = np.array([[1,1,2,2,3],
               [1,1,2,2,3],
               [1,1,2,2,3],
               [1,1,4,4,3],
               [1,1,5,5,5]])

print(isValid(test))


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
print(getIndices(test)[0])