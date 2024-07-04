#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''To onvert a key and its value to tuple of key and
    the square of its valeu.
    '''
    return (k, float(v**2))
