class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        pos = {}
        for i, num in enumerate(nums):
            pos[int(num)] = i
        
        for i, num in enumerate(nums):
            for larger_num in range(9, int(num), -1):
                if larger_num in pos:
                    j = pos[larger_num]
                    if j > i:
                        nums[i], nums[j] = nums[j], nums[i]
                        return int("".join(nums))

        return int("".join(nums))
"""
"1"
"""