class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(i, total, curr):
            if total >= target or i >= N:
                if total == target:
                    res.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i, total + nums[i], curr[:])
            curr.pop()
            dfs(i + 1, total, curr)

        dfs(0, 0, [])
        return res