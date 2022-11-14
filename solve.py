import numpy as np
from validateActions import *
from actions import *
import copy

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
         return 100000
     else:
         return int(max(counts)-min(counts))

def solveMondrian(n, M):
    initial_grid = initialiseGrid(n)
    actions = ['split', 'merge']
    states = [initial_grid]
    best_state = copy.copy(initial_grid)
    seen_states = [np.zeros((n,n))]
    depth = 0

    while (len(states)!=0):
        s = states[0]
        states.remove(s)
        if depth<M:
            print("Iteration " + str(int(depth)) + ", current best state score = " + str(score(best_state)))
            for action in actions:
                s_prime = copy.copy(eval(action)(s))
                if (np.any(np.all(s_prime != seen_states, axis=1))):
                    states.append(s_prime)
                    seen_states.append(s)
                    depth += 0.5
                    if (score(s_prime)<score(best_state)) and (isValid(s_prime)):
                        best_state = copy.copy(s_prime)



    return best_state, score(best_state)

print(solveMondrian(4,10))
