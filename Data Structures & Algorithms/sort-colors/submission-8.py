class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r and l < r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                while i < r and nums[i] == 0:
                    i += 1
                
                while l < r and nums[l] == 0:
                    l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                # print(nums)
                i += 1 
            
            # print(nums, i, l, r)


"""
012345678910
00012011222
  l
       r
  i

0112
 l
  r
   i

102
l
 r
 i

002112
  l
    r
i
"""