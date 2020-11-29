# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:35:59 2020

@author: cenic
"""
# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):

    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[[0 for orient in range(len(forward))]
               for j in range(len(grid[0]))]
              for row in range(len(grid))]
    closed[init[0]][init[1]][init[2]] = 1
    backtrackshortestpath = [[[list() for orient in range(len(forward))]
                              for j in grid[0]]
                             for i in grid]
    backtrackshortestpath[init[0]][init[1]][init[2]] = init
    backtrackinstr = [[[" " for orient in forward]
                       for j in grid[0]]
                      for i in grid]
    x = init[0]
    y = init[1]
    orient = init[2]
    g = 0

    open = [[g, x, y, orient]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort(key=lambda row: row[0])
            open.reverse()
            next = open.pop()

            x = next[1]
            y = next[2]
            orient = next[3]
            g = next[0]
            prevval = [x, y, orient]
            closed[x][y][orient] = 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(action)):
                    orient2 = (orient + action[i]) % 4
                    x2 = x + forward[orient2][0]
                    y2 = y + forward[orient2][1]
                    if x2 >= 0 and (
                            x2 < len(grid) and y2 >= 0 and y2 < len(grid[0])
                            ):
                        if closed[x2][y2][orient2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost[i]

                            open.append([g2, x2, y2, orient2])
                            backtrackshortestpath[x2][y2][orient2] = prevval
                            backtrackinstr[x2][y2][orient2] = action_name[i]
    expand = [[" " for i in grid[0]] for j in grid]
    currpos = [goal[0], goal[1], orient]
    expand[goal[0]][goal[1]] = "*"
    while(backtrackinstr[currpos[0]][currpos[1]][currpos[2]] != " "):
        prevpos = backtrackshortestpath[currpos[0]][currpos[1]][currpos[2]]
        ins = backtrackinstr[currpos[0]][currpos[1]][currpos[2]]
        expand[prevpos[0]][prevpos[1]] = ins
        currpos = prevpos

    return expand
