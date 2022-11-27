import numpy as np
from validateActions import *
from actions import *
import copy


def f(n, d):
    g_n = d
    h_n = score(n)
    return g_n+h_n

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
         return 1000
     else:
         return int(max(counts)-min(counts))

def solveMondrian(n, M):
    initial_grid = initialiseGrid(n)
    initial_grid = split(initial_grid)
    print(initial_grid)
    actions = ['split', 'merge']
    states = [initial_grid]
    best_state = copy.copy(initial_grid)
    seen_states = [np.zeros((n,n))]
    depth = 0
    fs = []
    fs.append(f(initial_grid, depth))
    while (len(states)!=0):
        print("Length of states to explore", len(states))
        print("Length of states seen", len(seen_states))
        mix_index = fs.index(min(fs))
        s = states.pop(mix_index)
        fs.pop(mix_index)
        if depth<M:
            print("Iteration " + str(int(depth)) + ", current best state score = " + str(score(best_state)))
            for action in actions:
                s_primes = copy.copy(eval(action)(s))
                for s_prime in s_primes:
                    # when working allow invalid states maybe
                    if (np.any(np.all(s_prime != seen_states, axis=1))) and (isValid(s_prime)):
                        if len(states)<20:
                            states.append(s_prime)
                            fs.append(f(s_prime, depth))
                        else:
                            max_index = fs.index(max(fs))
                            states.pop(max_index)
                            fs.pop(max_index)
                            states.append(s_prime)
                            fs.append(f(s_prime, depth))

                        seen_states.append(s)

                        if (score(s_prime)<score(best_state)) and (isValid(s_prime)):
                            best_state = copy.copy(s_prime)
            depth+=1
        else:
            break

    return best_state, score(best_state)

solveMondrian(6,200)
