# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        self._postorderTraversal(root, result)

        return result

    def _postorderTraversal(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return

        self._postorderTraversal(root.left, result)
        self._postorderTraversal(root.right, result)
        result.append(root.val)

        return
        