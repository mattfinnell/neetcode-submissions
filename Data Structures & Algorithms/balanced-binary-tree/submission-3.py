# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.height(root)

        return is_balanced

    def height(self, root):
        if not root:
            return (True, 0)

        left_balanced, left_height = self.height(root.left)
        right_balanced, right_height = self.height(root.right)

        if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
            return (False, max(left_height, right_height) + 1)

        return (True, max(left_height, right_height) + 1)