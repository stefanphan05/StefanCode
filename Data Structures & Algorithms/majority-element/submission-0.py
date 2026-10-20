class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            if freq[num] > half: return num