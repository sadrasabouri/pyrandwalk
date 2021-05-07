# -*- coding: utf-8 -*-
"""pyrandwalk main."""

import doctest
import sys
from .pyrandwalk_obj import *
from .pyrandwalk_param import *
from art import tprint


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TEST":
            error_flag = doctest.testfile(
                "pyrandwalk_test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            sys.exit(error_flag)
        else:
            tprint("pyrandwalk")
            tprint("V:" + PYRANDWALK_VERSION)
    else:
        tprint("pyrandwalk")
        tprint("V:" + PYRANDWALK_VERSION)
