# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(l, r) -> bool:
            if not l and not r:
                return True
            
            if (not l and r) or (l and not r) or (l.val != r.val):
                return False
            
            if not is_same_tree(l.left, r.left) or not is_same_tree(l.right, r.right):
                return False
            
            return True
        
        def dfs(root):
            if not root and not subRoot: return True
            if not root: return False
            if root.val == subRoot.val:
                if is_same_tree(root, subRoot): return True
            
            if dfs(root.left): return True
            if dfs(root.right): return True

            return False
        
        if dfs(root): return True
        return False