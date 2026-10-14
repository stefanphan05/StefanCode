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
        hash_map = {None:None}

        curr = head
        while curr:
            new_curr = Node(x=curr.val)
            hash_map[curr] = new_curr
            curr = curr.next
        
        curr = head
        while curr:
            next_node = curr.next
            random_node = curr.random

            new_node = hash_map[curr]
            new_node.next = hash_map[next_node]
            new_node.random = hash_map[random_node]

            curr = curr.next
        
        return hash_map[head]
"""
hash_map
curr -> new_node

next_node = curr.next


"""