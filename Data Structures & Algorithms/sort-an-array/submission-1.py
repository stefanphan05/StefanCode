class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])

        return self.merge(left, right)

    def merge(self, num1, num2):
        res = []
        l, r = 0, 0
        while l < len(num1) and r < len(num2):
            if num1[l] <= num2[r]:
                res.append(num1[l])
                l += 1
            else:
                res.append(num2[r])
                r += 1
        
        while l < len(num1):
            res.append(num1[l])
            l += 1
        
        while r < len(num2):
            res.append(num2[r])
            r += 1
        
        return res

"""
98111231
"""