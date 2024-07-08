#!/usr/bin/env python3
'''Task 0.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waiting for random number of seconds.
    '''
    timing = random.random() * max_delay
    await asyncio.sleep(timing)
    return timing
