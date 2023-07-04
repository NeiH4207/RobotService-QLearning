import numpy as np

class Map():
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = np.zeros((height, width))
        self.starting_point = (0, 0)
        self.current_point = self.starting_point
        
    def get_map_size(self):
        return self.height, self.width
    
    def get_grid(self):
        return self.grid
    
    def get_current_point(self):
        return self.current_point
    
    def get_starting_point(self):
        return self.starting_point
    
    def set_starting_point(self, x, y):
        self.starting_point = (x, y)
        self.current_point = (x, y)
        self.grid = np.zeros((self.height, self.width))
        self.grid[self.starting_point[0], self.starting_point[1]] = 1
    
    def set(self, x, y, value):
        assert value in [0, 1], 'value must be 0 or 1'
        assert 0 <= x < self.width and 0 <= y < self.height, 'x and y must be in range'
        self.grid[y, x] = value
        self.current_point = (x, y)
    
    def show(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.current_point:
                    print('X', end='')
                else:
                    if self.grid[y, x] == 1:
                        print('#', end='')
                    else:
                        print('.', end='')
            print()
        print()
            
            
    def reset(self):
        self.grid = np.zeros((self.height, self.width))
        self.current_point = self.starting_point