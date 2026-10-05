# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        self._serialize(root, result)

        return ",".join(result)

    def _serialize(self, root, result):
        if not root:
            result.append("None")
            return

        result.append(str(root.val))
        self._serialize(root.left, result)
        self._serialize(root.right, result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values, index = [
            int(value) if value != "None" else None
            for value in data.split(",")
        ], [0]

        return self._deserialize(values, index)

    def _deserialize(self, values, index):
        if values[index[0]] is None:
            index[0] += 1
            return None

        root = TreeNode(values[index[0]])
        index[0] += 1

        root.left, root.right = (
            self._deserialize(values, index),
            self._deserialize(values, index),
        )

        return root
