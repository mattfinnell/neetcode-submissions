# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, -math.inf, math.inf)

    def _isValidBST(self, root, minimum, maximum) -> bool:
        if not root:
            return True

        if not (minimum < root.val < maximum):
            return False

        return self._isValidBST(root.left, minimum, root.val) and self._isValidBST(root.right, root.val, maximum)
