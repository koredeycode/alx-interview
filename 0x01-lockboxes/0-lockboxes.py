#!/usr/bin/python3
"""
This module contain the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    The canUnlockAllFunction function
    Args:
        boxes: list of list of int
    Return:
        boolean
    """
    n = len(boxes)
    unlocked_boxes = [True] + [False] * (n - 1)

    seen_boxes = set([0])

    boxes_to_visit = list(boxes[0])

    while boxes_to_visit and not all(unlocked_boxes):
        box_index = boxes_to_visit.pop(0)
        if not box_index or box_index >= n or box_index < 0:
            continue
        if not unlocked_boxes[box_index]:
            unlocked_boxes[box_index] = True
            seen_boxes.add(box_index)
            boxes_to_visit.extend(boxes[box_index])

    return len(seen_boxes) == len(boxes)
