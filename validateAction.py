import numpy as np

def loss(grid):
     unique, counts = np.unique(grid, return_counts=True)
     return int(max(counts)-min(counts)), unique


def inorder(i):
     for element in i:
          if(element != list(range(element[0], element[-1] + 1))):
               return False
     return True


def checkOverlap(i, grid):
     index = []
     current_index = []
     for row in grid:
          current_index = np.where(row==i)[0].tolist()
          if (current_index):
               index.append(current_index)
     if (inorder(index)) and not (any(index[0]!= i for i in index)):
          return [len(index[0]), len(index)]
     else:
          return []


def isValid(grid):
     dimensions = []
     score, unique = loss(grid)
     for i in unique:
          dimensions.append(checkOverlap(i, grid))
     for j in range(len(dimensions)):
          n = dimensions.pop()
          if [n[1],n[0]] in dimensions or n in dimensions:
               return False
          
     return True