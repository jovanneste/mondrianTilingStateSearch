import numpy as np

def loss(grid):
     unique, counts = np.unique(grid, return_counts=True)
     return int(max(counts)-min(counts)), unique


test = np.array([[1,1,2,2,3],
               [1,1,2,2,3],
               [1,1,2,2,3],
               [1,1,4,4,3],
               [1,1,5,5,5]])



def inorder(i):
     for element in i:
          if(element != list(range(element[0], element[-1] + 1))):
               return False
     return True


def checkOverlap(i):
     index = []
     current_index = []
     for row in test:
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
          dimensions.append(checkOverlap(i))
     for j in range(len(dimensions)):
          n = dimensions.pop()
          if [n[1],n[0]] in dimensions or n in dimensions:
               return False
          
     return True
     


print(isValid(test))




# print(myList == list(range(myList[-1] + 1))) #check the indexs are in order
# print(any(index[0]!= i for i in index)) #check indexs are all the same at every row
# print() # dimensions 

# store dim 
# check its not overlapping 