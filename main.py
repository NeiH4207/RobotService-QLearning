"""
Created on Tue Apr 27 2:19:47 2023
@author: hien
"""
from __future__ import division
import json
import logging
import time
from algorithms.RandomStep import RandomStep
from src.environment import ServiceRobot
log = logging.getLogger(__name__)
from random import seed
from argparse import ArgumentParser

def argument_parser():
    parser = ArgumentParser()
    parser.add_argument('--show-screen', type=bool, default=True)
    parser.add_argument('-a', '--algorithm', default='stc')
    parser.add_argument('-v', '--verbose', action='store_true', default=True)
    parser.add_argument('--figure-path', type=str, default='figures/')
    parser.add_argument('--height', type=int, default=10)
    parser.add_argument('--width', type=int, default=10)
    parser.add_argument('--starting-point', default=(0, 0), type=int)
    return parser.parse_args()

def main():
    args = argument_parser()
    env = ServiceRobot(args.height, args.width, args.show_screen)
    algorithm = RandomStep(n_actions=env.n_actions)
    state = env.reset(args.starting_point[0], args.starting_point[1])
    while True:
        action = algorithm.get_action(state)
        next_state, reward, is_terminal, is_truncated = env.step(action)
        env.render()
        if is_terminal or is_truncated:
            break

if __name__ == "__main__":
    main()