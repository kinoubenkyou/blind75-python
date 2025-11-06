# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._traverse(root)
        return self.diameter

    def _traverse(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        left_height = self._traverse(node.left)
        right_height = self._traverse(node.right)
        diameter = left_height + right_height
        if diameter > self.diameter:
            self.diameter = diameter
        if left_height > right_height:
            return left_height + 1
        return right_height + 1
