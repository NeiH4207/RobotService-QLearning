import numpy as np


class STC():
    # STC: Spanning Tree Coverage algorithm
    def __init__(self, n_actions: int = 4) -> None:
        self.n_actions = n_actions
        self.edges = {}
        self.n_edges = 0
    
    def get_neighbors(self, current_point):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        neighbors = []
        for i in range(4):
            x = current_point[0] + dx[i]
            y = current_point[1] + dy[i]
            if self.in_bounds(x, y):
                neighbors.append((x, y))
                
        return neighbors
    
    def get_action(self, state, epsilon=0.0):
        current_point = state['current_point']
        neighbors = self.get_neighbors(current_point)
        if len(neighbors) == 0:
            return np.random.randint(0, self.n_actions)
        else:
            return np.random.choice(neighbors, p=self.get_probabilities(neighbors, state))