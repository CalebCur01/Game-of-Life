import arcade
import random
import numpy as np

ROW_COUNT = 100
COLUMN_COUNT = 100
DENSITY = 0.2
SCREEN_TITLE = "Game Of Life"

WIDTH = 20
HEIGHT = 20

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid = np.zeros((COLUMN_COUNT,ROW_COUNT))
grid2 = np.zeros((COLUMN_COUNT,ROW_COUNT))


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.clear()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if grid[row][column] == 1:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x,y,WIDTH,HEIGHT,color)

    def on_update(self,delta_time):
        update_state()

def initialize_grid(grid):
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):
            rand_val = random.random()
            if rand_val <= DENSITY:
                grid[i][j] = 1

def copy_grid(grid1, grid2): #copies values from left to right
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):
            grid2[i][j] = grid1[i][j]

def distance(x1,y1,x2,y2):
    xval = (x2 - x1) * (x2-x1)
    yval = (y2 - y1) * (y2-y1)
    xysum = xval+yval
    return math.sqrt(xysum)

def within_bounds(x,y):
    if x < 0 or x >= ROW_COUNT:
        return False
    if y < 0 or y >= COLUMN_COUNT:
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
    for i in range(COLUMN_COUNT):
        for j in range(ROW_COUNT):
            neighbors_alive = living_neighbors(i,j)
            if is_alive(i,j):
                if neighbors_alive < 2 or neighbors_alive > 3:
                    kill(i,j,grid2)
            if not is_alive(i,j): #if dead
                if neighbors_alive == 3:
                    revive(i,j,grid2)
    copy_grid(grid2,grid)

def main():
    initialize_grid(grid)
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.run()

    
if __name__ == "__main__":
    main()

