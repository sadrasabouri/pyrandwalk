# -*- coding: utf-8 -*-
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
>>> rw.prob_sec([2, 1, 0])
0.0125
>>> rw.prob_sec([2, 1, 0], initial_dist=[0, 0, 1, 0, 0])
0.0625
>>> np.random.seed(0)
>>> states, probs = rw.run()
>>> states
[4, 3, 4, 3, 4, 3, 4, 3, 2, 3, 4]
>>> probs
[0.2, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.75, 0.75]
>>> np.random.seed(1)
>>> states, probs = rw.run(ntimes=20)
>>> states
[3, 4, 3, 4, 3, 2, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 3]
>>> probs
[0.2, 0.75, 1.0, 0.75, 1.0, 0.25, 0.25, 0.75, 0.75, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.75]
>>> np.random.seed(10)
>>> states, probs = rw.run(ntimes=30, show=True)
1 --> 2  (p = 0.750)
2 --> 3  (p = 0.750)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 2  (p = 0.250)
2 --> 1  (p = 0.250)
1 --> 2  (p = 0.750)
2 --> 3  (p = 0.750)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 4  (p = 0.750)
4 --> 3  (p = 1.000)
3 --> 2  (p = 0.250)
2 --> 3  (p = 0.750)
>>> states
[1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 3]
>>> probs
[0.2, 0.75, 0.75, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.25, 0.75, 0.75, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.75]
>>> rw.final_dist()
array([1., 0., 0., 0., 0.])
>>> rw.is_irreducible()
False
>>> rw.trans_power(2)
array([[1.    , 0.    , 0.    , 0.    , 0.    ],
       [0.25  , 0.1875, 0.    , 0.5625, 0.    ],
       [0.0625, 0.    , 0.375 , 0.    , 0.5625],
       [0.    , 0.0625, 0.    , 0.9375, 0.    ],
       [0.    , 0.    , 0.25  , 0.    , 0.75  ]])
>>> rw.get_edges()
[(0, 0, 1.0), (1, 0, 0.25), (1, 2, 0.75), (2, 1, 0.25), (2, 3, 0.75), (3, 2, 0.25), (3, 4, 0.75), (4, 3, 1.0)]
>>> rw_graph = rw.get_graph()
>>> rw.get_colormap()
['red', 'blue', 'blue', 'blue', 'blue']
>>> rw_class_types = rw.get_typeof_classes()
>>> rw_class_types['recurrent']
([0], array([[1.]]))
>>> rw_class_types['transient'][0]
[1, 2, 3, 4]
>>> rw_class_types['transient'][1]
array([[0.  , 0.75, 0.  , 0.  ],
       [0.25, 0.  , 0.75, 0.  ],
       [0.  , 0.25, 0.  , 0.75],
       [0.  , 0.  , 1.  , 0.  ]])
>>> from pyrandwalk.pyrandwalk_util import *
>>> make_prob_dist([1, 2, 2])
array([0.2, 0.4, 0.4])
>>> make_prob_dist([1, 1000, 2])
array([9.97008973e-04, 9.97008973e-01, 1.99401795e-03])
>>> make_prob_dist([1, 1000, 2], precision=10**(-2))
array([0., 1., 0.])
"""