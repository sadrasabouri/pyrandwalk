# -*- coding: utf-8 -*-
"""Basic test file."""
"""
>>> from pyrandwalk import *
>>> import numpy as np
>>> states = [0, 1, 2, 3, 4]
>>> trans = np.array([[1,    0, 0,    0, 0],
...                   [0.25, 0, 0.75, 0, 0],
...                   [0, 0.25, 0, 0.75, 0],
...                   [0, 0, 0.25, 0, 0.75],
...                   [0, 0,    0, 1,    0]])
>>> rw = RandomWalk(states, trans)
>>> states = [0, 1, 2]
>>> trans = np.array([[1, 0, 0], [1/2, 0, 1/2], [0, 1, 0]])
>>> rw = RandomWalk(states, trans, payoff=[0, 1, 4])
>>> policy = rw.best_policy()
>>> policy['stop']
[0, 2]
>>> policy['continue']
[1]
>>> states = [0, 1, 2]
>>> trans = np.array([[1, 0, 0], [1/2, 0, 1/2], [0, 1, 0]])
>>> rw = RandomWalk(states, trans, payoff=[0, 1, 4], cost=[1, 0, 2], discount=0.5)
>>> policy = rw.best_policy(stop_states=[0])
>>> policy['stop']
[0, 1, 2]
>>> policy['continue']
[]

"""
