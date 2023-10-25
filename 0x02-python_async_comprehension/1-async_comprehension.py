#!/usr/bin/env python3
'''Task 1 module solution.
'''
from typing import List
from importlib import import_module as use


async_generator = use('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''This function creates a list of 10 floats generated
    from async_generator().
    '''
    return [numb async for numb in async_generator()]
