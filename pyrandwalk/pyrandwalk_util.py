# -*- coding: utf-8 -*-
"""Utility module."""
import numpy as np


def make_prob_dist(freq, precision=10**(-10)):
    """
    Return a fine probability distribution based on given frequencies of states.

    :param freq: inputted array showing rate of occurrence
    :type freq: list or np.array
    :param precision: shows the min threshold of probabilies
    :type precision: float
    :return: a np.array giving the probability disterbution
    """
    freq = np.array(freq)
    final_dist = freq / np.sum(freq)
    zero_probe_idx = final_dist < precision
    final_dist[zero_probe_idx] = 0
    final_dist = final_dist / np.sum(final_dist)
    return final_dist


def is_prob_dist(dist, precision=10**(-10)):
    """
    Check if given array is a probability distribution.

    :param dist: given array
    :type dist: list or np.array
    :return: True if dist is a probability distribution
    """
    dist = np.array(dist)
    if np.sum(dist < 0) != 0:
        return False
    if np.abs(np.sum(dist) - 1) > precision:
        return False
    return True


def is_valid_vector_type(vector):
    """
    Check if given vector is a valid one.

    :param vector: given vector
    :type vector: anything
    :return: True if vector is list or numpy array
    """
    return isinstance(vector, (list, np.ndarray))
