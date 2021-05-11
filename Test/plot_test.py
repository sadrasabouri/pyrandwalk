# -*- coding: utf-8 -*-
"""
>>> from pyrandwalk import *
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> rw = RandomWalk([0, 1], np.array([[0.25, 0.75],[0.3, 0.7]]))
>>> ax = rw.plot_graph()
>>> ax.get_title()
'My Random Walk Graph'
>>> ax = rw.plot_graph(title="test")
>>> ax.get_title()
'test'
"""