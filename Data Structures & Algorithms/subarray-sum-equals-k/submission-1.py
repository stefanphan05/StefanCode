class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefix_sum[diff]
            prefix_sum[curr_sum] += 1 
        
        return res

"""
2,-1,1,2

0 -> 1
2 -> 2
1 -> 1


"""