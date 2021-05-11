# -*- coding: utf-8 -*-
"""Random Walk module."""
from .pyrandwalk_param import *
from .pyrandwalk_util import *
from .pyrandwalk_error import pyrandwalkStateError, pyrandwalkTransitionsError
import numpy as np
from numpy import linalg as la
import networkx as nx


class RandomWalk():
    """
    Random Walk class.

    >>> states = [0, 1, 2, 3, 4]
    >>> trans = np.array([[1,    0, 0,    0, 0],
                          [0.25, 0, 0.75, 0, 0],
                          [0, 0.25, 0, 0.75, 0],
                          [0, 0, 0.25, 0, 0.75],
                          [0, 0,    0, 1,    0]])
    >>> rw = RandomWalk(states, trans)
    """

    def __init__(self, states, transitions):
        """
        Init method.

        :param states: list of states of random walk
        :type states: list or np.array
        :param transitions: matrix of transitions
        :type transitions: np.array
        """
        if not isinstance(states, (list, type(np.array([])))):
            raise pyrandwalkStateError(INVALID_STATE_TYPE_ERROR)
        self.S = states
        if not isinstance(transitions, (list, type(np.array([])))):
            raise pyrandwalkTransitionsError(INVALID_TRANSITIONS_TYPE_ERROR)
        self.P = np.array(transitions)

    def prob_sec(self, sequence, initial_dist=None):
        """
        Calculate probability of given sequence.

        :param sequence: given sequence of states
        :type sequence: list / np.array
        :param initial_dist: initial probability disturbition of states
        :type initial_dist: list
        :return: probability of given sequence of states happening
        """
        if initial_dist is None:
            initial_dist = [1 / len(self.S)] * len(self.S)
        current_state = sequence[0]
        probability = initial_dist[current_state]
        for next_state in sequence[1:]:
            probability *= self.P[self.S.index(current_state),
                                  self.S.index(next_state)]
            current_state = next_state
        return probability

    def run(self, ntimes=10, show=False):
        """
        Run random walk for ntimes and print out result on each transition.

        :param ntimes: numbers of running
        :type ntimes: int
        :param show: flag which is set when showing run is desired
        :return: (generated_states, probability)
        """
        state = np.random.choice(self.S)
        states = [state]
        probabilities = [1 / len(self.S)]
        for i in range(ntimes):
            next_state = np.random.choice(self.S, p=self.P[state])
            probability = self.P[state, next_state]
            states.append(next_state)
            probabilities.append(probability)
            if show is True:
                print(RUN_PRINT.format(state, next_state, probability))
            state = next_state
        return states, probabilities

    def final_dist(self, precision=10**(-10)):
        """
        Return final probability distribution of the random walk.

        :param precision: shows the min threshold of probabilies
        :type precision: float
        :return: final distribution as np.array
        """
        v, Q = la.eig(self.P)
        Q = Q[:, v.argsort()[::-1]]
        final_probs = la.inv(Q)[0, :]
        return make_prob_dist(final_probs, precision=precision)

    def is_irreducible(self):
        """
        Return true if stochastic process associated with random walk is irreducible.

        :return: a bool which is true when the process is irreducible
        """
        return nx.is_strongly_connected(self.get_graph())

    def trans_power(self, n):
        """
        Return nth power of transition matrix.

        :param n: power of desired matrix
        :type n: int
        :return: nth power of transition matrix
        """
        return la.matrix_power(self.P, n)

    def get_edges(self):
        """
        Return none-zero weighted edges of random walk.

        :return: list of tuples consisting of from_node, to_node and weight
        """
        edges = []
        state_idx = range(len(self.S))
        for i in state_idx:
            for j in state_idx:
                if self.P[i, j] > 0:
                    edges.append((i, j, self.P[i, j]))
        return edges

    def get_graph(self):
        """
        Return directional graph generated from random walk.

        :return: directional weighted graph as networkx.DiGraph
        """
        graph = nx.DiGraph()
        graph.add_weighted_edges_from(self.get_edges())
        return graph

    def get_colormap(self):
        """
        Return graph node color map.A node is red iff it has a ring edge.

        :return: list of color strings.
        """
        graph = self.get_graph()
        colormap = ['blue' for _ in graph]
        for i, node in enumerate(graph):
            if graph.has_edge(node, node):
                colormap[i] = 'red'
        return colormap

    def plot_graph(self, suptitle="Graph", title="My Random Walk Graph"):
        """
        Plot graph associated with random walk.

        :param suptitle: figure suptitle
        :type suptitle: string
        :param title: figure title
        :type title: string
        :return: generated plot
        """
        import matplotlib.pyplot as plt
        colormap = self.get_colormap()
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(suptitle)
        ax.set_title(title)
        nx.draw_circular(self.get_graph(),
                         node_color=colormap,
                         with_labels=True,
                         font_weight='bold')
        return ax

    def get_typeof_classes(self):
        """
        Return classes separated according to their types.

        :return: dictionary consisting of classes and their types
        """
        class_list = nx.strongly_connected_components(self.get_graph())
        class_dict = {}
        for class_ in class_list:
            class_ = list(class_)
            idx = [self.S.index(c) for c in class_]
            sub_trans = np.take(np.take(self.P, idx, axis=0), idx, axis=1)
            is_recurrent = np.all(sub_trans.sum(axis=1) == 1)
            if is_recurrent:
                class_dict['recurrent'] = (class_, sub_trans)
            else:
                class_dict['transient'] = (class_, sub_trans)
        return class_dict
