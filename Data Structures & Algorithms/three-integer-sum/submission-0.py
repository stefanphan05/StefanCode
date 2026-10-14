class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for x in range(n - 2):
            if x > 0 and nums[x] == nums[x - 1]: continue

            l, r = x + 1, n - 1
            while l < r:
                total = nums[x] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[x], nums[l], nums[r]])
                    
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res