class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = [1] * n
        right = [1] * n

        current_product = 1
        for i in range(n):
            if i == 0: continue
            current_product *= nums[i - 1]
            left[i] = current_product
        
        current_product = 1
        for i in range(n - 1, -1, -1):
            if i == n - 1: continue
            current_product *= nums[i + 1]
            right[i] = current_product
        
        for i in range(n):
            res[i] = left[i] * right[i]

        return res