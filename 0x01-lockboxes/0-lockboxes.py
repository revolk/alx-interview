#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    queue = [0]  # Start with the first box
    opened[0] = True

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
