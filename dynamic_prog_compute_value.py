# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:05:55 2020

@author: cenic
"""

# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    value = [[99 for j in grid[0]]for i in grid]
    visitednodes = [goal]
    visnodesset = [goal]
    value[goal[0]][goal[1]] = 0
    while visitednodes:
        currentnode = visitednodes.pop(0)
        for mov in delta:
            x2 = mov[0] + currentnode[0]
            y2 = mov[1] + currentnode[1]
            if x2 >= 0 and y2 >= 0 and x2 < len(grid) and y2 < len(grid[0]):
                if [x2, y2] not in visnodesset and grid[x2][y2] == 0:
                    visnodesset.append([x2, y2])
                    visitednodes.append([x2, y2])
                    value[x2][y2] = value[currentnode[0]][currentnode[1]]+cost
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    return value
