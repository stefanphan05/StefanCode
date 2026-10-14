class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for num in nums:
            if num - 1 in nums: continue

            i = 0
            while num + i in nums:
                i += 1
            
            res = max(res, i)

        return res
"""
0,-1
   i
   j

0,0 -> n = 2
i
  j

[0,3,2,5,4,6,1,1]


[2,20,4,10,3,4,5]


"""