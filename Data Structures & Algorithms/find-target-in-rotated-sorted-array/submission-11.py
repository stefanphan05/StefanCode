class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m

            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    if target > nums[m] or target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if target > nums[r] or target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            print(m, l, r)
        
        return -1

"""
3   1
l
    r
m

target = 0

0   1   2   3   4   5   6
4   5   6   7   0   1   2
                l
                        r
                    m

3   5   6   7   0   1   2   3
l
            r
                m

0   1   2   3   4   6   7
l
                        r
            m

if nums[l] < nums[r]: -> do a normal search


"""