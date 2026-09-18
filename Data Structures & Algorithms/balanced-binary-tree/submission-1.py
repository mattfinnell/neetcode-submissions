# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _isBalanced(root) -> Tuple[int, bool]:
            if not root:
                return (0, True) 

            (height_left, is_left_balanced), (height_right, is_right_balanced) = (
                _isBalanced(root.left), 
                _isBalanced(root.right)
            )

            if not is_left_balanced or not is_right_balanced or abs(height_left - height_right) > 1:
                return (0, False)

            return (max(height_left, height_right) + 1, is_left_balanced and is_right_balanced)
        
        return _isBalanced(root)[1]