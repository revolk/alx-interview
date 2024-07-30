# test_0_lockboxes.py
from 0_lockboxes import canUnlockAll

def test_canUnlockAll():
    assert canUnlockAll([[1], [2], [3], [4], []]) == True
    assert canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]) == True
    assert canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]) == False
