# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre_left = dummy
        for i in range(left-1):
            pre_left = pre_left.next
        
        pre = None
        curr = pre_left.next
        for i in range(right -left + 1):
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        
        pre_left.next.next = curr

        pre_left.next = pre

        return dummy.next