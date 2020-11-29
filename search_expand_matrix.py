# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]]
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
    expand =[[-1 for j in grid[0]]for i in grid]
    expand[init[0]][init[1]]=0
    visitctr = 1
    while opengcost:
        node = min(opengcost, key=opengcost.get)
        if node not in visited:
            visited.add(node)
            for val in delta:
                x = [node[0]+val[0], node[1]+val[1]]
                x2= tuple(x)
                currcost = opengcost[node] + cost
                if (x == goal):
                    expand[x[0]][x[1]] = visitctr
                    return expand
                if x[0]>=0 and x[1]>=0 and x[0]<=len(grid)-1 and x[1]<=len(grid[0])-1 and grid[x[0]][x[1]]==0:
                    if x2 not in visited:
                        opengcost[x2]=currcost
                        if expand[x[0]][x[1]]==-1:
                                  expand[x[0]][x[1]] = visitctr
                                  visitctr+=1
                        
        opengcost.pop(node)
    return expand