class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        def dfs(i, curr):
            if i >= N:
                res.append(curr)
                return

            # Take
            curr.append(nums[i])
            dfs(i + 1, curr[:])
            
            curr.pop()
            # Nah
            dfs(i + 1, curr)

        dfs(0, [])
        return res
"""



-> 2^n
"""