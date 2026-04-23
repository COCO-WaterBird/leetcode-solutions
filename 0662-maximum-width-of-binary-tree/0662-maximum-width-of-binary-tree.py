# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_width = 0
        
        # 用队列来进行广度优先搜索 (BFS)
        queue = deque([(root, 0)])  # 存储节点和它的索引

        while queue:
            # 计算当前层的最左和最右节点的索引
            left = queue[0][1]
            right = queue[-1][1]

            # 更新最大宽度
            max_width = max(max_width, right - left + 1)

            # 遍历当前层的所有节点
            for _ in range(len(queue)):
                node, idx = queue.popleft()

                # 向队列添加左子节点和右子节点，并更新它们的索引
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
        
        return max_width