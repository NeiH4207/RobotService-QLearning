

from src.map import Map


class ServiceRobot():
    
    def __init__(self, height=10, width=10, show_screen=True):
        self.map_size = (height, width)
        self.show_screen = show_screen
        self.map = Map(self.map_size[0], self.map_size[1])
        self.space_size = self.map_size
        self.n_actions = 4
        self.n_steps = 0
        self.action_map = {
            0: 'U',
            1: 'D',
            2: 'L',
            3: 'R'
        }
        
    def render(self):
        if self.show_screen:
            self.map.show()
        
    def get_state(self):
        state = {}
        state['grid'] = self.map.get_grid()
        state['current_point'] = self.map.get_current_point()
        return state
    
    def reset(self, x, y):
        self.map.set_starting_point(x, y)
        return self.get_state()
    
    def in_bound(self, x, y):
        return 0 <= x < self.space_size[0] and 0 <= y < self.space_size[1]
    
    def is_truncated(self):
        return self.n_steps >= (self.space_size[0] * self.space_size[1]) ** 2
    
    def is_terminal(self):
        return self.map.get_current_point() == self.map.get_starting_point() and self.n_steps > 0
    
    def step(self, action):
        current_point = self.map.get_current_point()
        self.n_steps += 1
        
        if action == 0:
            next_point = (current_point[0] - 1, current_point[1])
        elif action == 1:
            next_point = (current_point[0] + 1, current_point[1])
        elif action == 2:
            next_point = (current_point[0], current_point[1] - 1)
        elif action == 3:
            next_point = (current_point[0], current_point[1] + 1)
        else:
            raise ValueError('Invalid action')
        
        if not self.in_bound(next_point[0], next_point[1]):
            return self.get_state(), -1, False, self.is_truncated()
        else:
            if self.map.get_grid()[next_point[0], next_point[1]] == 1:
                reward = - 0.5
            else:
                reward = 1
            
            self.map.set(next_point[0], next_point[1], 1)
            
            return self.get_state(), reward, self.is_terminal(), self.is_truncated()