# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        left, right = sentinel, head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left, right = left.next, right.next

        left.next = left.next.next

        return sentinel.next