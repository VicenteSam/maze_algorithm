import numpy as np
import random

class Backtracking():
    def __init__(self, row, column):
        self.row = row if row % 2 == 1 else row + 1
        self.column = column if column % 2 == 1 else column + 1

    def createMaze(self):
        maze = np.ones((self.row, self.column), dtype=int)

        sx = random.choice(range(1, self.row-1, 2))
        sy = random.choice(range(1, self.column-1, 2))
        maze[sx][sy] = 0

        self.carve_passages(sx, sy, maze)
        
        return maze

    def carve_passages(self, cx, cy, grid):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]   
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 < nx < self.row-1 and 0 < ny < self.column-1 and grid[ny][nx] == 1:
                wall_x, wall_y = cx + dx // 2, cy + dy // 2
                grid[wall_x][wall_y] = 0
                grid[ny][nx] = 0
                self.carve_passages(nx, ny, grid)
    
    def print_maze(self, maze):
        for row in maze:
            print("".join("█" if cell == 1 else
                        " " for cell in row))

                

if __name__ == '__main__':
    maze = Backtracking(7, 7)
    result = maze.createMaze()
    maze.print_maze(result)
