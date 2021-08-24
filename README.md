


<div align="center">
<img src="https://github.com/sadrasabouri/pyrandwalk/raw/master/Otherfiles/logo.png" width="300" height="300" alt="pyrandwalk-logo"><br/>
<br/>
<h1>:walking: Python Library for Random Walks</h1>

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://www.codefactor.io/repository/github/sadrasabouri/pyrandwalk/overview/master"><img src="https://www.codefactor.io/repository/github/sadrasabouri/pyrandwalk/badge/master" alt="CodeFactor" /></a>
<a href="https://codecov.io/gh/sadrasabouri/pyrandwalk">
  <img src="https://codecov.io/gh/sadrasabouri/pyrandwalk/branch/master/graph/badge.svg" />
</a>
<a href="https://colab.research.google.com/github/sadrasabouri/pyrandwalk/blob/master/Document/Document.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Document"/>
</a>
</div>

----------
## Table of contents					
   * [Overview](https://github.com/sadrasabouri/pyrandwalk#overview)
   * [Installation](https://github.com/sadrasabouri/pyrandwalk#installation)
   * [Usage](https://github.com/sadrasabouri/pyrandwalk#usage)
   * [Contribution](https://github.com/sadrasabouri/pyrandwalk/blob/master/.github/CONTRIBUTING.md)
   * [References](https://github.com/sadrasabouri/pyrandwalk#references)
   * [Authors](https://github.com/sadrasabouri/pyrandwalk/blob/master/AUTHORS.md)
   * [Changelog](https://github.com/sadrasabouri/pyrandwalk/blob/master/CHANGELOG.md)
   * [License](https://github.com/sadrasabouri/pyrandwalk/blob/master/LICENSE)

## Overview

<p align="justify">	
Pyrandwalk is an educational tool for simulating random walks, calculating the probability of given state sequences, etc. Random walk is a representation of the discrete-time, discrete-value Markov chain model used in stochastic processes.
</p>


<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/pyrandwalk"><img src="http://pepy.tech/badge/pyrandwalk"></a></td>
	</tr>
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

### Source code
- Download [Version 1.1](https://github.com/sadrasabouri/pyrandwalk/archive/v1.1.zip) or [Latest Source ](https://github.com/sadrasabouri/pyrandwalk/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)
- Run `pip install pyrandwalk` or `pip3 install pyrandwalk` (Need root access)


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
We are simulating random walks on the above graph (weights are probabilities):
<img src="https://github.com/sadrasabouri/pyrandwalk/raw/master/Otherfiles/usage_example.webp">


### Probability of A Sequence

Imagine you want to calculate probability which you start from state 2, go to state 1 and stuck in state 0.
What's the probability of these walk sequences?
```pycon
>>> rw.prob_sec([2, 1, 0])
0.0125
```

Initial probability distribution is assumed to be uniform by default but you can change it by passing optional argument `initial_dist`:
```pycon
>>> rw.prob_sec([2, 1, 0], initial_dist=[0, 0, 1, 0, 0])
0.0625
```


### Run a random walk

You can start a random walk on given markov chain and see the result:

```pycon
>>> states, probs = rw.run()
>>> states
[4, 3, 4, 3, 4, 3, 4, 3, 2, 3, 4]
>>> probs
[0.2, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.75, 0.75]
```

By default your random walk will contain 10 steps, but you can change it by passing optional argument `ntimes`:

```pycon
>>> states, probs = rw.run(ntimes=20)
>>> states
[3, 4, 3, 4, 3, 2, 1, 2, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 2, 3]
>>> probs
[0.2, 0.75, 1.0, 0.75, 1.0, 0.25, 0.25, 0.75, 0.75, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.75, 1.0, 0.25, 0.75]
```

And if you want to see what's going on down there during the simulation you can set the `show` flag:

```pycon
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
```


### Final Probability Distribution

You can easily find out the final probability distribution of you random walk by:
```pycon
>>> rw.final_dist()
array([1., 0., 0., 0., 0.])
```
Which implies that the walk will in state `0` for sure as time goes on.

### Is it irreducible?

You can check if your Markov chain is irreducible to lower rank ones or not by:

```pycon
>>> rw.is_irreducible()
False
```


### nth transition matrix

If you want to see what's the probability of moving from state `i` to `j` with `n` steps, you can easily calculate the nth transition matrix by:
```pycon
>>> rw.trans_power(2)
array([[1.    , 0.    , 0.    , 0.    , 0.    ],
       [0.25  , 0.1875, 0.    , 0.5625, 0.    ],
       [0.0625, 0.    , 0.375 , 0.    , 0.5625],
       [0.    , 0.0625, 0.    , 0.9375, 0.    ],
       [0.    , 0.    , 0.25  , 0.    , 0.75  ]])
```


### Graph edges

You can have your final graph edges in a list containing tuples like `(from, to, probability)` for each edge by:

```pycon
>>> rw.get_edges()
[(0, 0, 1.0), (1, 0, 0.25), (1, 2, 0.75), (2, 1, 0.25), (2, 3, 0.75), (3, 2, 0.25), (3, 4, 0.75), (4, 3, 1.0)]
```

### Graph

Making a *networkx* graph object from your random walk process is also token care of by this library:

```pycon
>>> rw_graph = rw.get_graph()
```

### __Colors of Nodes__ [will be removed]

Until now we could not show graphs with self-loops using networkx so as far as this feature being added to networkx, we're using `blue` color for ordinary states and `red` color for states with self-loop.

```pycon
>>> rw.get_colormap()
['red', 'blue', 'blue', 'blue', 'blue']
```


### Type of Classes

For knowing which class is recurrent or transient you can use above method, you can also have reduced transition matrix for each set.

```pycon
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


### The Best Policy Problems

For making the best policy problems for your random walk you can easily:

```pycon
>>> states = [0, 1, 2]
>>> trans = np.array([[1, 0, 0], [1/2, 0, 1/2], [0, 1, 0]])
>>> rw = RandomWalk(states, trans, payoff=[0, 1, 4], cost=[1, 0, 2], discount=0.5)
>>> rw.best_policy()
{'continue': [], 'stop': [0, 1, 2]}
```


## References			

<blockquote>1- Lawler, Gregory F. Introduction to stochastic processes. Chapman and Hall/CRC, 2018.</blockquote>
<blockquote>2- <a href="https://markusfeng.com/projects/graph/">Markusfeng</a></blockquote>
<div>Icon made by <a href="https://www.flaticon.com/authors/becris" title="Becris">Becris</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
