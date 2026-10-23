class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        sum_even, sum_odd = 0, 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                sum_even += num
            else:
                sum_odd += num
        
        curr_even, curr_odd = 0, 0
        count = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_after = sum_even - curr_even - num
                odd_after = sum_odd - curr_odd
                if curr_odd + even_after == curr_even + odd_after:
                    count += 1

                curr_even += num
            else:
                even_after = sum_even - curr_even
                odd_after = sum_odd - curr_odd  - num
                if curr_odd + even_after == curr_even + odd_after:
                    count += 1

                curr_odd += num
        
        return count