class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                if abs(hash_map[num] - i) <= k:
                    return True
            
            hash_map[num] = i
        return False