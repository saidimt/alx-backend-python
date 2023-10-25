#!/usr/bin/env python3
'''Task 0's module The basics of async.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait_random waits for a random delay between 0 and max_delay 10.
    '''
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
