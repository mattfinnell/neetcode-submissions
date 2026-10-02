# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        previous = slow.next = None
        a, b = head, self.reverse(second)
        while b:
            a_tmp, b_tmp = a.next, b.next
            a.next, b.next = b, a_tmp
            a, b = a_tmp, b_tmp

    def reverse(self, head):
        previous, current = None, head
        while current:
            temporary, current.next = current.next, previous
            previous, current = current, temporary

        return previous