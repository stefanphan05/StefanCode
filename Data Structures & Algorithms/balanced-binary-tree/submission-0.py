# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            
            return max(1 + height(root.left), 1 + height(root.right))
        
        def dfs(root):
            if not root:
                return True
            
            l, r = height(root.left), height(root.right)
            if abs(l - r) > 1:
                return False

            if not dfs(root.left) or not dfs(root.right):
                return False

            return True
        
        return dfs(root)