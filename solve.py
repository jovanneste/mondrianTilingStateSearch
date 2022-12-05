import numpy as np
from validateActions import *
from actions import *
import copy
import random
import matplotlib.pyplot as plt

# returns an nxn grid to be the root of our search tree
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

# mondrian score of a given state
def score(grid):
     unique, counts = np.unique(grid, return_counts=True)
     if len(unique)==1:
         # just one tile fills the grid
         return 100
     else:
         return int(max(counts)-min(counts))

# state best first seach
def SolveMondrian(a, M):
    scores, allscores = [], []
    depth=0
    initial_grid = initialiseGrid(a)
    best_grid = initial_grid
    best_score = score(initial_grid)
    actions = ['merge', 'split']
    closedList = []
    openList = [initial_grid]
    while openList != []:
        if depth < M:
            q = openList.pop()
            for action in actions:
                grid = copy.deepcopy(q)
                s_primes = []
                # apply merge and split the state
                s_primes = eval(action)(grid)
                if len(s_primes)==0:
                    break

                for s in s_primes:
                    print(s)
                    if (any((s == x).all() for x in closedList)):
                        # we have already seen this state
                        break

                scores = [score(x) for x in s_primes]
                # 10% of the time we do not take the lowest scoring option
                if random.uniform(0,1)<0.1:
                    best_s_prime = random.choice(s_primes)
                else:
                    best_s_prime = s_primes[np.argmin(scores)]

                if score(best_s_prime)<best_score and isValid(best_s_prime):
                        best_grid = best_s_prime
                        best_score = score(best_s_prime)

                allscores.append(best_score)
                openList.append(best_s_prime)
                closedList.append(best_s_prime)
                depth+=1
        else:
            break

    # plot the value of M vs the best scores
    plt.title(str(a) + "x" + str(a))
    plt.xlabel("Iterations")
    plt.ylabel("Mondrian Score")
    plt.plot([i for i in range(M)], allscores)
    plt.grid()
    plt.show()

    return best_grid
