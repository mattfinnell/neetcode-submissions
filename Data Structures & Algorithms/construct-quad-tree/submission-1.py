"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self._construct(grid, len(grid), 0, 0)

    def _construct(self, grid: List[List[int]], n, row, col) -> 'Node':
        if n == 1:
            return Node(grid[row][col], True)

        mid = n // 2

        top_left     = self._construct(grid, mid, row, col)
        top_right    = self._construct(grid, mid, row, col + mid)
        bottom_left  = self._construct(grid, mid, row + mid, col)
        bottom_right = self._construct(grid, mid, row + mid, col + mid)

        if (
            top_left.isLeaf and 
            top_right.isLeaf and 
            bottom_left.isLeaf and 
            bottom_right.isLeaf and 
            top_left.val == top_right.val == bottom_left.val == bottom_right.val
        ):
            return Node(top_left.val, True)

        return Node(
            0, 
            False,
            top_left,
            top_right,
            bottom_left,
            bottom_right
        )