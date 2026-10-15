# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def length(root) -> int:
            if not root:
                return 0
            
            return max(1 + length(root.left), 1 + length(root.right))
        
        def longest(root) -> int:
            return length(root.left) + length(root.right)
        
        def recursive(root):
            if not root:
                return 0
            
            max_num = longest(root)
            max_num = max(max_num, recursive(root.left))
            max_num = max(max_num, recursive(root.right))

            return max_num

        return recursive(root)