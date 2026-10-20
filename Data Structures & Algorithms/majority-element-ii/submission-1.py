class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        res = set()

        for num in nums:
            freq[num] += 1
            if freq[num] > len(nums) / 3:
                res.add(num)
        
        return list(res)