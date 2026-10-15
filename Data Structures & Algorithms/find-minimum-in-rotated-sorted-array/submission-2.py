class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_value = 1001
        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    min_value = min(min_value, nums[m])
                    r = m - 1
            else:
                min_value = min(min_value, nums[l])
                r = l - 1

        return min_value


"""
1, 2, 3, 4, 5, 6, 7
nums[l] < nums[r] -> return nums[l]

3, 4, 5, 6, 7, -1, 1, 2
                l
                      r
                    m

min_value = 1001
nums[l] > nums[r]
    nums[m] > nums[l]
        l = m + 1
    else:
        min_value = min(min_value, nums[m])
        r = m - 1
else:
    min_value = min(min_value, nums[l])
    r = l

sort -> nlogn
loopthrough -> n

logn

2 1
l
  r
m
"""