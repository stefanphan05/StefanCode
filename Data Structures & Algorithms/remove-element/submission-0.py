class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, i = 0, 0
        while i < len(nums):
            if nums[l] != val:
                l += 1

            if nums[i] != val and i > l:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            else:
                i += 1

        return l

"""
01223042, val = 2

01304222 -> k = 5

01304222
    l
       i
"""