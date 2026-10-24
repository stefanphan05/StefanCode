class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []
        for a in range(N - 3):
            for b in range(a + 1, N - 2):
                c, d = b + 1, N - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        if [nums[a], nums[b], nums[c], nums[d]] not in res:
                            res.append([nums[a], nums[b], nums[c], nums[d]])

                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1

                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                        
                    elif total > target:
                        d -= 1
                    else:
                        c += 1
                
            
        return res