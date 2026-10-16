"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        node_map = {}

        def dfs(curr):
            if curr in node_map:
                return node_map[curr]
            
            copy_curr = Node(val=curr.val)
            node_map[curr] = copy_curr
            for nei in curr.neighbors:
                copy_curr.neighbors.append(dfs(nei))
            
            return copy_curr
        
        dfs(node)
        return node_map[node]