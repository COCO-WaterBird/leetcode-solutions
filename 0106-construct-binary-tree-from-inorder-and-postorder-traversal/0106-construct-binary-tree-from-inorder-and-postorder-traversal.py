# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root.val)
        left_size = len(inorder[:root_index])

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_postorder = postorder[:left_size]
        right_postorder = postorder[left_size:-1]

        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)

        return root