import numpy as np


class RandomStep():
    def __init__(self, n_actions: int = 4) -> None:
        self.n_actions = n_actions
        
    def get_action(self, state, epsilon=0.0):
        return np.random.randint(0, self.n_actions)