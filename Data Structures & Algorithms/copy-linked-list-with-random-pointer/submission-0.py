"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        current = head
        while current:
            new = Node(current.val)
            new.next, current.random = current.random, new
            current = current.next
            
        current, sentinel = head, head.random
        while current:
            new = current.random
            new.random = new.next.random if new.next else None
            current = current.next

        current = head
        while current:
            new = current.random
            current.random = new.next
            new.next = current.next.random if current.next else None
            current = current.next

        return sentinel
