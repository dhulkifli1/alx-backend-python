#!/usr/bin/env python3
'''TypeChecking'''

from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in
