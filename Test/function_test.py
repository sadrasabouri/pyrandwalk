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
>>> policy = rw.best_policy()
>>> policy['stop']
[0, 1, 2, 3, 4]
>>> policy['continue']
[]
>>> states = [1, 2, 3]
>>> trans = np.array([[0.4, 0.2, 0.4],
...                   [0.6,  0 , 0.4],
...                   [0.2, 0.5, 0.3]])
>>> rw = RandomWalk(states, trans)
>>> rw.final_dist()
array([0.37878788, 0.25757576, 0.36363636])
>>> states = [1, 2, 3]
>>> trans = np.array([[0.2, 0.4, 0.4],
...                   [0.1, 0.5, 0.4],
...                   [0.6, 0.3, 0.1]])
>>> rw = RandomWalk(states, trans)
>>> rw.final_dist()
array([0.28205128, 0.41025641, 0.30769231])
>>> states = [0, 1, 2]
>>> trans = np.array([[1, 0, 0], [1/2, 0, 1/2], [0, 1, 0]])
>>> rw = RandomWalk(states, trans, payoff=[0, 1, 4])
>>> policy = rw.best_policy()
>>> policy['stop']
[0, 2]
>>> policy['continue']
[1]
>>> rw = RandomWalk(states, trans, payoff=[0, 1, 4], cost=[1, 3, 4], discount=0.1)
>>> policy = rw.best_policy()
>>> policy['stop']
[0, 1, 2]
>>> policy['continue']
[]
>>> np.random.seed(0)
>>> states = ['I', 'eat', 'food']
>>> trans = np.array([[0.1, 0.8, 0.1], [0.15, 0.05, 0.8], [0.8, 0.15, 0.05]])
>>> rw = RandomWalk(states, trans)
>>> states, probs = rw.run(show=True)
I --> eat  (p = 0.800)
eat --> food  (p = 0.800)
food --> eat  (p = 0.150)
eat --> food  (p = 0.800)
food --> I  (p = 0.800)
I --> eat  (p = 0.800)
eat --> food  (p = 0.800)
food --> I  (p = 0.800)
I --> eat  (p = 0.800)
eat --> food  (p = 0.800)
>>> states
['I', 'eat', 'food', 'eat', 'food', 'I', 'eat', 'food', 'I', 'eat', 'food']
>>> probs
[0.3333333333333333, 0.8, 0.8, 0.15, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]
>>> rw.final_dist()
array([0.34133043, 0.33805889, 0.32061069])
>>> policy = rw.best_policy()
>>> policy['stop']
['I', 'eat', 'food']
>>> policy['continue']
[]
>>> from pyrandwalk.pyrandwalk_util import *
>>> make_prob_dist([1, 2, 2])
array([0.2, 0.4, 0.4])
>>> make_prob_dist([1, 1000, 2])
array([9.97008973e-04, 9.97008973e-01, 1.99401795e-03])
>>> make_prob_dist([1, 1000, 2], precision=10**(-2))
array([0., 1., 0.])
>>> is_prob_dist([1, 2, 3])
False
>>> is_prob_dist([0.5, 0.25, 0.25])
True
>>> is_prob_dist([1/3, 1/3, 1/3])
True
>>> is_prob_dist([1/3, -1/3, 1/3])
False
>>> is_prob_dist([1/3, -1/3, -1/3])
False
>>> is_valid_vector_type([1, 2, 3])
True
>>> is_valid_vector_type(np.array([1, 2, 3]))
True
>>> is_valid_vector_type(1)
False
"""