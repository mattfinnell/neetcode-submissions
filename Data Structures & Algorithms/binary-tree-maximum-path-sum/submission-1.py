# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        self._maxPathSum(root, result)

        return result[0] 


    def _maxPathSum(self, root, result):
        if not root:
            return 0

        left_max, right_max = (
            max(0, self._maxPathSum(root.left, result)),
            max(0, self._maxPathSum(root.right, result)),
        )

        result[0] = max(
            result[0],
            root.val + left_max + right_max,
        )

        return root.val + max(left_max, right_max)