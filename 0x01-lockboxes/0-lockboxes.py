#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''

    opened = [False] * len(boxes)
    opened[0] = True
    keys = set(boxes[0])

    while True:
        newKeys = []
        if len(keys) == 0:
            break
        for key in keys:
            if not opened[key]:
                opened[key] = True
                newKeys += boxes[key]

        keys = set(newKeys)

    for box in opened:
        if not box:
            return False
    return True
