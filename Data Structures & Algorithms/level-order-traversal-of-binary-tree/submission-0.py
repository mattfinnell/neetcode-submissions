from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, result = deque([root]), []

        while queue:
            queue_length, layer = len(queue), []

            for _ in range(queue_length):
                node = queue.popleft()
                if node:
                    layer.append(node.val)
                    queue.extend([node.left, node.right])

            if layer:
                result.append(layer)

        return result