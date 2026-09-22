# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root, root.val)

    def _goodNodes(self, root, maximum) -> int:
        if not root:
            return 0

        result = 1 if root.val >= maximum else 0
        maximum = max(maximum, root.val)

        result += self._goodNodes(root.left, maximum) + self._goodNodes(root.right, maximum)

        return result