# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = _get_height(node.left)
            if left_height == -1:
                return -1
            right_height = _get_height(node.right)
            if right_height == -1:
                return -1
            if -1 <= left_height - right_height <= 1:
                return left_height + 1 if left_height > right_height else right_height + 1
            return -1
        return _get_height(root) != -1
