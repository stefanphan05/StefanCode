# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if not root:
                return 0
            
            return max(1 + height(root.left), 1 + height(root.right))
        
        deep = height(root)
        res = []
        for _ in range(height(root)):
            res.append([])

        def bfs(root, level):
            if not root:
                return
            
            res[level].append(root.val)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)
        
        bfs(root, 0)
        return res