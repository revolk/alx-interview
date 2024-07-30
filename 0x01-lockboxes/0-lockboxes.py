#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    queue = deque([0])  # بدء قائمة الانتظار بالبوكس الأول
    unlocked[0] = True

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if not unlocked[key] and key < n:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
