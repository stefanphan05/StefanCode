# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p

        def dfs(root):
            if not root:
                return
            
            if p.val == root.val:
                return p
            if q.val == root.val:
                return q
            if p.val < root.val < q.val:
                return root
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            if p.val < root.val and q.val < root.val:
                return dfs(root.left)
        
        return dfs(root)

"""
                5
        3               8
    1       4       7       9
        2


2, 1 -> 1
3, 7 -> 5

one on the left and one on the right
one is the paren of the other
"""