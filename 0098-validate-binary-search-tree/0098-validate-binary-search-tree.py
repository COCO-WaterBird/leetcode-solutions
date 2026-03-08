# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = inf
        pre = -inf
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal ans,pre
            ans = min(ans,node.val-pre)
            pre = node.val
            dfs(node.right)

        dfs(root)
        return ans>0