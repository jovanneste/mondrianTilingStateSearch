import numpy as np
import random


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


def getIndices(grid):
    unique = np.unique(grid)
    indices = {}
    for n in unique:
        i = np.nonzero(grid == n)
        indexes = []
        for j in range(len(i[0])):
            indexes.append([i[0][j], i[1][j]])
        indices.update({n: indexes})
    return sorted(indices.items(), key=lambda item: len(item[1]), reverse=True)


class MondrianTile:
    def __init__(self, n, *args):
        self.n = n
        if args:
            self.grid = args[0]
        else:
            self.grid = initialiseGrid(n)

    def __str__(self):
        return str(self.grid)

    def split(self):
        grid = self.grid
        largest_rectangle = getIndices(grid)[0][1]
        new_num = len(np.unique(grid))+1
        # make this more elegant
        dimensions = [largest_rectangle[-1][0]-largest_rectangle[0]
                      [0]+1, largest_rectangle[-1][1]-largest_rectangle[0][1]+1]
        tile_num = (max(dimensions)//2) * min(dimensions)
        if max(dimensions) % 2 == 0:
            tile_num = tile_num - min(dimensions)
        for i in range(tile_num):
            index = largest_rectangle[i]
            grid[index[0], index[1]] = new_num
        new_tile = object.__new__(MondrianTile, self.n, grid)
        return new_tile

    def merge(self):
        smallest_rectangle = getIndices(self.grid)[-1][1]
        surroundings = []
        merge_options = []
        for index in smallest_rectangle:
            surroundings.append([sum(i) for i in zip(index, [1, 0])])
            surroundings.append([sum(i) for i in zip(index, [0, 1])])
            surroundings.append([sum(i) for i in zip(index, [-1, 0])])
            surroundings.append([sum(i) for i in zip(index, [0, -1])])
        for index in surroundings:
            if index not in smallest_rectangle:
                if self.grid.shape[0] not in index:
                    # check point is a point in the grid and is not the smallest rectangle itself
                    merge_options.append(index)
        choice = random.choice(merge_options)
        number = self.grid[choice[0], choice[1]]
        for i in smallest_rectangle:
            self.grid[i[0], i[1]] = number
        return self.grid


if __name__ == '__main__':
    tile = MondrianTile(7)
    print("Original tile\n", tile)
    newtile = tile.split()
    print("Original tile\n", tile)
    print("New tile\n", newtile)
