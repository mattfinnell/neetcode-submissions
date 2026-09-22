from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, result = deque([root]), []

        while queue:
            queue_length, layer = len(queue), []

            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(layer)

        return [r[-1].val for r in result]
