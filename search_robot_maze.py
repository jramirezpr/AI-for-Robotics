# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:18:03 2020

@author: cenic
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    opengcost = {tuple(init):0}
    visited = set()
    
    while opengcost:
        node = min(opengcost,key=opengcost.get)
        if node not in visited:
            visited.add(node)
            for val in delta:
                x = [node[0]+val[0], node[1]+val[1]]
                x2= tuple(x)
                currcost = opengcost[node] + cost
                if (x == goal):
                    return [currcost, x[0], x[1]]
                if x[0]>=0 and x[1]>=0 and x[0]<=len(grid)-1 and x[1]<=len(grid[0])-1 and grid[x[0]][x[1]]==0:
                    if x2 not in opengcost:
                        opengcost[x2]=currcost
        opengcost.pop(node)
    return "fail"