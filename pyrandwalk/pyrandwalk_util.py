# -*- coding: utf-8 -*-
"""Utility module."""
import numpy as np

def make_prob_dist(dist, precision=10*(-10)):
    """

    :param dist: inputted array showing rate of occurrence
    :type dist: np.array
    :param precision: shows the min threshold of probabilies
    :type precision: float
    :return: a np.array giving the probability disterbution
    """
    dist = np.array(dist)
    final_dist = dist / np.sum(dist)
    zero_probe_idx = final_dist < precision
    final_dist[zero_probe_idx] = 0
    final_dist = final_dist / np.sum(final_dist)
    return final_dist
