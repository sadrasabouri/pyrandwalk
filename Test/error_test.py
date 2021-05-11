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
"""