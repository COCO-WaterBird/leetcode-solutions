# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = -inf
        def dfs(node):
            nonlocal pre
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= pre:
                return False
            pre = node.val
            return dfs(node.right)
        return dfs(root)