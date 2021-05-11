# -*- coding: utf-8 -*-
"""Parameters and constants."""
PYRANDWALK_VERSION = "0.1"

RUN_PRINT = "{0} --> {1}  (p = {2:.3f})"

INVALID_STATE_TYPE_ERROR = "Invalid type for state parameter. It should be either a list or a numpy array."
INVALID_TRANSITIONS_TYPE_ERROR = "Invalid type for transitions parameter. It should be either a list or a numpy array."
TRANSITIONS_SIZE_ERROR = "Transition matrix size should be (STATES_SIZE, STATES_SIZE)."
TRANSITIONS_ROW_PROBABILITY_ERROR = "Row {0} of transition matrix ({1}) is not a probability distribution."
