class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        position = {}
        for i, num in enumerate(nums):
            position[int(num)] = i
        
        for i, num in enumerate(nums):
            for larger_num in range(9, int(num), -1):
                if larger_num in position and position[larger_num] > i:
                    j = position[larger_num]
                    nums[i], nums[j] = nums[j], nums[i]
                    return int("".join(nums))
        
        return int("".join(nums))

        

"""
983819
  l
   r

minimum number, l 
maximum number, r
and l < r

01234
98368

3,2 - 
"""