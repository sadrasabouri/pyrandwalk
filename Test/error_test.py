# -*- coding: utf-8 -*-
"""
>>> from pyrandwalk import *
>>> import numpy as np
>>> rw = RandomWalk('test', [1])
Traceback (most recent call last):
        ...
pyrandwalk.pyrandwalk_error.pyrandwalkStateError: Invalid type for state parameter. It should be either a list or a numpy array.
>>> rw = RandomWalk([1], 'test')
Traceback (most recent call last):
        ...
pyrandwalk.pyrandwalk_error.pyrandwalkTransitionsError: Invalid type for transitions parameter. It should be either a list or a numpy array.
>>> trans = [[1,2,3], [1,2,3], [1,2,3]]
>>> rw = RandomWalk(['State0', 'State1'], trans)
Traceback (most recent call last):
        ...
pyrandwalk.pyrandwalk_error.pyrandwalkTransitionsError: Transition matrix size should be (STATES_SIZE, STATES_SIZE).
>>> rw = RandomWalk(['State0', 'State1', 'State2'], trans)
Traceback (most recent call last):
        ...
pyrandwalk.pyrandwalk_error.pyrandwalkTransitionsError: Row 0 of transition matrix ([1, 2, 3]) is not a probability distribution.
"""