# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        s1 = head
        s2 = s.next
        s.next = None

        # Reverse the second half
        prev = None
        curr = s2
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        s2 = prev
        while s2:
            n1, n2 = s1.next, s2.next
            s1.next = s2
            s2.next = n1

            s1 = n1
            s2 = n2
"""
2 - 4 - 6
   s1

9 - 8
   s2

2 - 9 - 4 - 8 - 6

"""