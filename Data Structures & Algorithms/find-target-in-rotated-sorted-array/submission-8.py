class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            
        return -1
"""
target = 3
1, 3



target=0,4
4,5,6,7,0,1,2
        l
            r
          m


target = 5 
5, 1, 3
l
      r
   m

target = 4
5, 1, 3
l
      r
   m


target = 1
3,1
l
  r
  m

target = 0
4,5,6,7,0,1,2
l
            r
      m l
        r

target = 2

4, 5, 6, 7, 8, 9, 0, 1, 2, 3
l
                           r
       m          r

4, 5, 6, 7, 8, 9, 0, 1, 2, 3
l
                           r
                     m


"""