#!/usr/bin/env python3
'''Task 0 module coroutine will loop 10 times.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Async generator that creates a sequence of 10 numbers.
    '''
    for h in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
