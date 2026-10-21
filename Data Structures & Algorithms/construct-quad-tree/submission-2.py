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
        leaf_nodes = {
            0: Node(False, True),
            1: Node(True, True),
        }

        return self._construct(grid, len(grid), 0, 0, leaf_nodes)

    def _construct(self, grid: List[List[int]], n, row, col, leaf_nodes) -> 'Node':
        if n == 1:
            return leaf_nodes[grid[row][col]]

        n //= 2

        top_left     = self._construct(grid, n, row, col, leaf_nodes)
        top_right    = self._construct(grid, n, row, col + n, leaf_nodes)
        bottom_left  = self._construct(grid, n, row + n, col, leaf_nodes)
        bottom_right = self._construct(grid, n, row + n, col + n, leaf_nodes)

        if (
            top_left.isLeaf and 
            top_right.isLeaf and 
            bottom_left.isLeaf and 
            bottom_right.isLeaf and 
            top_left.val == top_right.val == bottom_left.val == bottom_right.val
        ):
            return top_left

        return Node(
            0, 
            False,
            top_left,
            top_right,
            bottom_left,
            bottom_right
        )