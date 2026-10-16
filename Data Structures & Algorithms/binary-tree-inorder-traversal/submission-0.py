# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        self._inorderTraversal(root, result)

        return result

    def _inorderTraversal(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return

        self._inorderTraversal(root.left, result)
        result.append(root.val)
        self._inorderTraversal(root.right, result)

        return
        