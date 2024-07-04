#!/usr/bin/env python3
'''Task 6.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''TO compute the sum of list of ints and floating-point nbrs.
    '''
    return float(sum(mxd_lst))
