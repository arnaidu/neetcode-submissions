# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1
        before_left = None
        start_left_node = head
        while pos < left:
            next_node = start_left_node.next
            before_left = start_left_node
            start_left_node = next_node
            pos += 1

        localPrev = None
        localCurr = start_left_node
        while pos <= right:
            next_node = localCurr.next
            localCurr.next = localPrev
            localPrev = localCurr
            localCurr = next_node
            pos += 1
        
        start_left_node.next = localCurr

        if before_left:
            before_left.next = localPrev
            return head

        return localPrev


