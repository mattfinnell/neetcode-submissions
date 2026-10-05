# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self._buildTree(
            preorder,  0, 
            0, len(inorder) - 1, 
            {v: i for i, v in enumerate(inorder)}
        )

    def _buildTree(self, preorder: List[int], prefix_index, left, right, table) -> Optional[TreeNode]:
        if left > right:
            return None

        value = preorder[prefix_index]
        root, mid = TreeNode(value), table[value]

        root.left, root.right = (
            self._buildTree(
                preorder, prefix_index + 1, 
                left, mid - 1, 
                table
            ),
            self._buildTree(
                preorder, prefix_index + (mid - left) + 1, 
                mid + 1, right, 
                table
            ),
        )

        return root
