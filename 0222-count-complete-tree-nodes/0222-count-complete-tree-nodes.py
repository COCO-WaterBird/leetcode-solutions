# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         left,right = root,root
#         height_l,height_r = 0,0
#         while left.left:
#             height_l += 1
#             left = left.left
#         while right.right:
#             height_r += 1
#             right = right.left
#         if height_l == height_r:
#             return 2 ** height_l + self.countNodes(root.right)
#         else:
#             return 2 ** height_r + self.countNodes(root.left)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = root, root
        height_l, height_r = 0, 0

        while left:
            height_l += 1
            left = left.left

        while right:
            height_r += 1
            right = right.right

        if height_l == height_r:
            return 2 ** height_l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)