import math
import numpy as np

class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def MakeGrid(self):
        blank_grid = np.full((self.height, self.width), "   ")
        return blank_grid
    
    def AddThinVerticalWall(self, x_start, y_start, wall_length):
        y_end = y_start + wall_length
        for y in range(y_start, y_end):
            self[y, x_start] = ""



