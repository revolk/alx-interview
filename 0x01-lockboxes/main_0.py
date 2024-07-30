#!/usr/bin/python3

def canUnlockAll(boxes):
    """تحديد ما إذا كان يمكن فتح جميع الصناديق."""
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    queue = [0]  # ابدأ بالصندوق الأول
    opened[0] = True

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)

# اختبار الدالة
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
