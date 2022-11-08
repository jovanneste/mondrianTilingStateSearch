import numpy as np 
from PIL import Image # used to display images
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd

def loss(grid):
	unique, counts = np.unique(grid, return_counts=True)
	return int(max(counts)-min(counts)), unique

# Function to save grid as image where each tile is a different colour 
def visualiseColours(grid, name):
	grid_name = 'tileImages/'+str(name)+'.png'
	score, unique = loss(grid)
	myColors = ["red", "blue", "white", "yellow", "green", "black"]
	myCmap = colors.ListedColormap(myColors)

	plt.imshow(grid, cmap=myCmap, vmin=1, vmax=5)
	plt.title("Score: " + str(score))
	plt.savefig(grid_name)
	Image.open(grid_name).show()
	return 

# Function to save grid as csv
def visualiseGrid(grid, name):
	grid_name = 'tileImages/'+str(name)+'.csv'
	df = pd.DataFrame(grid)
	df.to_csv(grid_name,index=False, header=False)
	return 

bef_merge = np.array([[1,1,1,2,2],
     [1,1,1,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2],
     [3,3,3,4,4]])

optimal = np.array([[1,1,1,2,2],
     [1,1,1,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2]])

bef_split = np.array([[1,1,1,2,2],
     [1,1,1,2,2],
     [1,1,1,2,2],
     [1,1,1,2,2],
     [1,1,1,2,2]])


#visualiseColours(bef_merge, 'before_merge')
#visualiseColours(optimal, 'after')
#visualiseColours(bef_split, 'before_split')