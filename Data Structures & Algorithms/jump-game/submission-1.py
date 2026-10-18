class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        goal = N - 1
        for i in range(N - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False