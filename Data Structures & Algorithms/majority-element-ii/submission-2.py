class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        res = set()

        for num in nums:
            freq[num] += 1
            
            if len(freq.items()) > 2:
                new_freq = defaultdict(int)
                for i in freq.keys():
                    freq[i] -= 1
                    if freq[i] > 0:
                        new_freq[i] = freq[i]
                
                freq = new_freq
        
        res = []
        for num in freq:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res