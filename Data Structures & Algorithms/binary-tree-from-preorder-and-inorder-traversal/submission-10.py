# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i
        
        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)
            mid = idx[root.val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)

"""
        1
    2       3
                4



"""