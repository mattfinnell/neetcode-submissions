# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(root) -> int:
            if not root:
                return 0 
            
            left, right = height(root.left), height(root.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return max(left, right) + 1
        
        height(root)

        return self.max_diameter