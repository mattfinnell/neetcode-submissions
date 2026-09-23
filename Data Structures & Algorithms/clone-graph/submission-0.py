"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        table = {}
        table[node], queue = Node(node.val), deque([node])

        while queue:
            current = queue.popleft()

            for n in current.neighbors:
                if n not in table:
                    table[n] = Node(n.val)
                    queue.append(n)

                table[current].neighbors.append(table[n])

        return table[node]
