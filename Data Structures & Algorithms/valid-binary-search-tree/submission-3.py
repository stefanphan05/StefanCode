# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node: return True

            if node.val >= upper or node.val <= lower:
                return False

            if not dfs(node.left, lower, min(upper, node.val)) or not dfs(node.right, max(lower, node.val), upper):
                return False
            return True
        
        return dfs(root, float("-inf"), float("inf"))

"""
            2
        1       3


-inf        2           inf
-inf        1           2
"""