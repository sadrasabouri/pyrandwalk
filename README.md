# pyrandwalk
Python Library for Random Walks.

----------
## Table of contents					
   * [Overview](https://github.com/sadrasabouri/pyrandwalk#overview)
   * [Installation](https://github.com/sadrasabouri/pyrandwalk#installation)
   * [Usage](https://github.com/sadrasabouri/pyrandwalk#usage)
   * [Contribution](https://github.com/sadrasabouri/pyrandwalk/blob/master/.github/CONTRIBUTING.md)
   * [References](https://github.com/sadrasabouri/pyrandwalk#references)
   * [Authors](https://github.com/sadrasabouri/pyrandwalk/blob/master/AUTHORS.md)
   * [License](https://github.com/sadrasabouri/pyrandwalk/blob/master/LICENSE)

## Overview

<p align="justify">	
Pyrandwalk is a tool for simulating random walks, calculate the probability of given state sequences and etc.
Random walk is a representation of discrete-time, discrete-value Markov chain model using in stochastic processes.
</p>


<table>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sadrasabouri/pyrandwalk"><img src="https://img.shields.io/github/stars/sadrasabouri/pyrandwalk.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
    <tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sadrasabouri/pyrandwalk/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sadrasabouri/pyrandwalk/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table>



## Installation		



## Usage


```pycon
>>> from pyrandwalk import *
>>> import numpy as np
>>> states = [0, 1, 2, 3, 4]
>>> trans = np.array([[1,    0, 0,    0, 0],
...                   [0.25, 0, 0.75, 0, 0],
...                   [0, 0.25, 0, 0.75, 0],
...                   [0, 0, 0.25, 0, 0.75],
...                   [0, 0,    0, 1,    0]])
>>> rw = RandomWalk(states, trans)
```
We are simulating random walks on above graph (weights are probabilities):
<img src="https://github.com/sadrasabouri/pyrandwalk/raw/master/Otherfiles/usage_example.webp">
```pycon
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

```


## References			

<blockquote>1- Gregory F.Lawler, "Introduction to Stochastic Processes".</blockquote>

