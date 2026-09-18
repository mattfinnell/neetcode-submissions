# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
            
        # P or Q equals root
        if root.val in [p.val, q.val]:
            return root

        # P or Q Diverges from root
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root

        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)