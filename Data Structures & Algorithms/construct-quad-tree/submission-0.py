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
        all_same = True

        for i in range(n):
            for j in range(n):
                if grid[row][col] != grid[row + i][col + j]:
                    all_same = False
                    break

        if all_same:
            return Node(grid[row][col], True)

        n //= 2

        return Node(
            0, 
            False,
            self._construct(grid, n, row, col),
            self._construct(grid, n, row, col + n),
            self._construct(grid, n, row + n, col),
            self._construct(grid, n, row + n, col + n),
        )
