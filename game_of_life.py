import numpy as np
import math
import random

columns = 10
rows = 10
density = 0.2


def initialize_grid(grid):
    for i in range(columns):
        for j in range(rows):
            rand_val = random.random()
            if rand_val <= density:
                grid[i][j] = 1

def copy_grid(grid1, grid2): #copies values from left to right
    for i in range(columns):
        for j in range(rows):
            grid2[i][j] = grid1[i][j]

def distance(x1,y1,x2,y2):
    xval = (x2 - x1) * (x2-x1)
    yval = (y2 - y1) * (y2-y1)
    xysum = xval+yval
    return math.sqrt(xysum)

def within_bounds(x,y):
    if x < 0 or x >= rows:
        return False
    if y < 0 or y >= columns:
        return False
    return True

def are_neighbors(x1,y1,x2,y2):
    if(distance(x1,y1,x2,y2)) <= 1:
       return True
    return False

def is_alive(x,y):
    return grid[x][y] == 1

def kill(x,y,grid2):
    grid2[x][y] = 0

def revive(x,y,grid2):
    grid2[x][y] = 1

def living_neighbors(x,y):
    sum = 0
    xvals = {x-1,x+1}
    for val in xvals:
        if within_bounds(val,y):
            sum = sum + grid[val][y]
        if within_bounds(val,y-1):
            sum = sum + grid[val][y-1]
        if within_bounds(val,y+1):
            sum = sum + grid[val][y+1]
    if(within_bounds(x,y-1)):
       sum = sum+ grid[x][y-1]
    if(within_bounds(x,y+1)):
       sum = sum + grid[x][y+1]
    return sum

def update_state():
    for i in range(columns):
        for j in range(rows):
            neighbors_alive = living_neighbors(i,j)
            if is_alive(i,j):
                if neighbors_alive < 2 or neighbors_alive > 3:
                    kill(i,j,grid2)
            if not is_alive(i,j): #if dead
                if neighbors_alive == 3:
                    revive(i,j,grid2)
    copy_grid(grid2,grid)
                    
                
    
    


grid = np.zeros((columns,rows))
grid2 = np.zeros((columns,rows))

initialize_grid(grid)
copy_grid(grid,grid2)





