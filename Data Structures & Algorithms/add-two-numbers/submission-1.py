# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, previous, carry = l1, None, 0
        while l1 and l2:
            (carry, value), previous = divmod(l1.val + l2.val + carry, 10), l1
            l1.val, l1, l2= value, l1.next, l2.next

        if l2:
            previous.next = l2
            l1 = previous.next

        while l1:
            (carry, value), previous = divmod(l1.val + carry, 10), l1
            l1.val, l1 = value, l1.next

        if carry:
            previous.next = ListNode(carry)

        return head