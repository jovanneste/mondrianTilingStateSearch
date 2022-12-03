import numpy as np
from validateActions import *
from actions import *
import copy
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

def score(grid):
     unique, counts = np.unique(grid, return_counts=True)
     if len(unique)==1:
         return 100
     else:
         return int(max(counts)-min(counts))

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
                s_primes = eval(action)(grid)
                if len(s_primes)==0:
                    break

                for s in s_primes:
                    if (any((s == x).all() for x in closedList)):
                        break
                    else:
                        print(s)

                scores = [score(x) for x in s_primes]
                if random.uniform(0,1)<0.9:
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

    print('\n\n\n')
    print(allscores)
    print(best_score)
    print(best_grid)
    visualiseColours(best_grid, 'best_8x8')

SolveMondrian(12,100)
