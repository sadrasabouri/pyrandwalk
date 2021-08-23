---
title: 'PyRandWalk: A Python Library for Random Walks Simulaton'
tags:
  - Python
  - educational
  - simulation
  - probability
  - Markov chains
  - stochastic processes
  - reinforcement learning
authors:
  - name: Sadra Sabouri
    orcid: 0000-0003-1047-2346
    affiliation: 1
affiliations:
 - name: Sharif University of Technology
   index: 1
date: 15 August 2021
bibliography: paper.bib

---

# Summary

Pyrandwalk is an educational tool for simulating random walks, calculating the probability of given state sequences, etc. Random walk is a representation of the discrete-time, discrete-value Markov chain model used in stochastic processes.

The first idea of this paper is inherited from Pyrgg.[@Haghighi2017]

# Statement of need

There are classes of problems in which occurrences did not deterministically happen. In these types of problems each of the probable next states will be assigned to a probability showing its chance of happening. In some cases we use a simplification called Markov Assumption which suggests that each state is just correlated to its last one so we don't take into consideration before states.

These types of problems are not only used in pure mathematics but also in many nowadays hot topics like Reinforcement Learning, Bigram Language Models, etc. Because understanding the mathematics behind the random walks and Markov chains needs good knowledge in statistics and probability and most of the new learners can not enter into these fields we decided to solve this issue by developing a Python library which gives a simple intuition about these rather hard problems called PyRandWalk.[@lawler2018introduction]

# References
