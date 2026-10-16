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
            if curr and curr not in node_map:
                copy_curr = Node(val=curr.val)
                node_map[curr] = copy_curr
            
                for neigh in curr.neighbors:
                    dfs(neigh)
        
        dfs(node)
        
        already_connected = set()
        def connect(curr):
            if curr and curr not in already_connected:
                for neigh in curr.neighbors:
                    node_map[curr].neighbors.append(node_map[neigh])
                already_connected.add(curr)
                for neigh in curr.neighbors:
                    connect(neigh)

        connect(node)
        return node_map[node]