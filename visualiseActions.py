import numpy as np 
from PIL import Image # used to display images
import matplotlib.pyplot as plt
from matplotlib import colors


def loss(grid):
	unique, counts = np.unique(grid, return_counts=True)
	return int(max(counts)-min(counts)), unique


def visualise(grid, name):
	grid_name = 'tileImages/'+str(name)+'.png'
	score, unique = loss(grid)
	myColors = ["red", "blue", "white", "yellow", "green", "black"]
	myCmap = colors.ListedColormap(myColors)

	plt.imshow(grid, cmap=myCmap, vmin=1, vmax=5)
	plt.title("Score: " + str(score))
	plt.savefig(grid_name)
	Image.open(grid_name).show()
	return 



bef_merge = np.array([[1,1,1,2,2],
     [1,1,1,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2],
     [3,3,3,4,4]])


aft_merge = np.array([[1,1,1,2,2],
     [1,1,1,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2],
     [3,3,3,2,2]])

visualise(bef_merge, 'before_merge')
visualise(aft_merge, 'after_merge')