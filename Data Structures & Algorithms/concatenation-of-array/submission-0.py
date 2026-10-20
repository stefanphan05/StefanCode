class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [-1] * 2 * N

        for i in range(N):
            ans[i] = ans[i + N] = nums[i]

        return ans