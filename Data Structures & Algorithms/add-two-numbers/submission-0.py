# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        borrow = 0
        while l1 or l2 or borrow:
            total = borrow
            if l1 and l2:
                total += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total += l1.val
                l1 = l1.next
            elif l2:
                total += l2.val
                l2 = l2.next
            
            remain, borrow = total % 10, total // 10
            new_node = ListNode(val=remain)
            curr.next = new_node
            curr = curr.next
        
        return dummy.next

"""
1 > 2 > 3
l

4 > 5 > 6
r

5, 0
"""