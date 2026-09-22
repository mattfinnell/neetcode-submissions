# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        
        self._kthSmallest(root, traversal)

        return traversal[k - 1]


    def _kthSmallest(self, root: Optional[TreeNode], traversal):
        if root:
            self._kthSmallest(root.left, traversal),
            traversal.append(root.val)
            self._kthSmallest(root.right, traversal)