# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 特判
        if not head or not head.next:
            return head
        if k == 0:
            return head
        
        # 第一步：找到尾节点，计算链表长度
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        
        # 第二步：尾节点连上头节点，形成环
        tail.next = head
        
        # 第三步：找到新的尾节点位置
        newtail = head
        for i in range(n - k % n - 1):
            newtail = newtail.next
        
        # 第四步：断开环，确定新头节点
        newhead = newtail.next
        newtail.next = None
        
        return newhead        