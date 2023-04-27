#!/usr/bin/python3
"""canUnlockAll function present"""
from typing import List, Set


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """The canUnlockAllFunction"""
    unlocked_boxes: List[bool] = [True] + [False] * (len(boxes) - 1)

    seen_boxes: Set[int] = set([0])

    boxes_to_visit: List[int] = list(boxes[0])

    while boxes_to_visit:
        box_index: int = boxes_to_visit.pop(0)
        if not unlocked_boxes[box_index]:
            unlocked_boxes[box_index] = True
            seen_boxes.add(box_index)
            boxes_to_visit.extend(boxes[box_index])

    return len(seen_boxes) == len(boxes)
