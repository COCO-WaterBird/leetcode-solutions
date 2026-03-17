# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        count = []
        def dfs(node,depth):
            if not node:
                return
            if depth == len(sums):
                sums.append(0)
                count.append(0)
            sums[depth] += node.val
            count[depth] += 1
            dfs(node.left, depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return [sums[i]/count[i] for i in range(len(sums))]