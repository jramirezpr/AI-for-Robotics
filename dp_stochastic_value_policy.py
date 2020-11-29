# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:13:32 2020

@author: cenic
"""

# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#

#
#  will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# is sufficiently close to true value
# (within 0.001).

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    for i in range(2000):
        change=False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y]="*"
                        change = True
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                        miss_action_1 =(a+1) %4
                        xm = x + delta[miss_action_1][0]
                        ym = y + delta[miss_action_1][1]
                        miss_action_2 =(a+3) %4
                        xn = x + delta[miss_action_2][0]
                        yn = y + delta[miss_action_2][1]
                        def ca_cost(x2, y2, grid, collision_cost, cost_step):
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                return cost_step + value[x2][y2]
                            else:
                                return cost_step + collision_cost
                        c_s = ca_cost(x2, y2, grid, collision_cost, cost_step)
                        c_1 = ca_cost(xm, ym, grid, collision_cost, cost_step)
                        c_2 = ca_cost(xn, yn, grid, collision_cost, cost_step)
                        v2 = success_prob * c_s + failure_prob*(c_1 + c_2)
                        if v2  < value[x][y]:
                            change = True
                            value[x][y] = v2
                            policy[x][y]= delta_name[a]
    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, 3] # Goal is in top right corner
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print(row)
for row in policy:
    print(row)

# Expected outputs:
#
#[471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
#[334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977], 
#[398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738], 
#[700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
