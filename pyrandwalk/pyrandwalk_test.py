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

"""
