import numpy as np
from validateActions import *
from actions import *
import copy
import sys

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




def solve(n, M):
    depth = 0
    actions = ['merge', 'split']
    initial_grid = initialiseGrid(n)
    openList = [initial_grid]
    corresonding_fs = [f(initial_grid, depth)]
    closedList = []
    bestscore=score(initial_grid)
    print(bestscore)
    while openList!=[]:
        if depth==M:
            print(bestscore)
            break
        depth+=1
        q_index = np.argmin(corresonding_fs)
        corresonding_fs.pop(q_index)
        q = openList.pop(q_index)
        q_copy = copy.copy(q)
        closedList.append(q_copy)
        for action in actions:
            s_primes = copy.copy(eval(action)(q))
            for s_prime in s_primes:
                if any((s_prime == x).all() for x in closedList):# or not (isValid(s_prime)):
                    continue
                else:
                    if (isValid(s_prime)):
                        if (score(s_prime)<bestscore):
                            bestscore = score(s_prime)
                            print("New best score", bestscore)
                    if any((s_prime == x).all() for x in openList):
                        continue
                    else:
                        openList.append(s_prime)
                        corresonding_fs.append(f(s_prime, depth))
    print('openlist is empty, best score =', bestscore)




solve(12,200000)
