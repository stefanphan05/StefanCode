# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        s, f = dummy, dummy
        for _ in range(n + 1):
            f = f.next
        
        while f:
            s = s.next
            f = f.next
        
        next_node = s.next.next
        s.next = next_node
        return dummy.next
        

"""
d - 1 - 2 - 3 - 4 - 5 - 6
                s
                            f
n = 2

d - 5
s
        f
n = 1
"""