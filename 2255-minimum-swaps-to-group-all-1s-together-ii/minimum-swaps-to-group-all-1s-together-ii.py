class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        k = sum(nums)

        l = 0
        best = 0
        curr = 0
        for r in range(N + k - 1):          # Go pass the end a k to cover the linking part
            if nums[r % N] == 1:
                curr += 1
            if r - l + 1 != k:
                continue
            
            best = max(best, curr)

            # Move the left pointer
            if nums[l % N] == 1:
                curr -= 1
            l += 1

        return k - best



"""
101000110


"""