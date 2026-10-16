class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in range(len(nums) + 1):
            if num not in nums_set: return num