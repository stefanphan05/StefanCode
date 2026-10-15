# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        temp = []
        def dfs(root, level):
            if not root: return
            
            while len(temp) <= level:
                temp.append([])
            
            temp[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        res = []
        dfs(root, 0)
        for arr in temp:
            res.append(arr[-1])
        
        return res