# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not root:
                return 0

            left_height, right_height = height(root.left), height(root.right)

            diameter = max(diameter, left_height + right_height)

            return max(left_height, right_height) + 1

        height(root)

        return diameter