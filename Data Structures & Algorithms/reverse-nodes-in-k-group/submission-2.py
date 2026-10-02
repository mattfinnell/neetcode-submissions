# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        previous, left = sentinel, head

        while left:
            right = self.getKth(left, k)
            if not right:
                break

            # Gotcha: create another pointer to right.next, twine groups with 'previous'
            next_group = right.next
            previous.next, previous = self.reverse(left, next_group)
            left = next_group

        return sentinel.next

    def getKth(self, current, k):
        while current and k > 1:
            current = current.next
            k -= 1

        return current

    def reverse(self, head, target):
        # Gotcha: have previous == target to help twine pointers together
        previous, current = target, head
        while current and current is not target:
            temporary, current.next = current.next, previous
            previous, current = current, temporary

        return (previous, head)






