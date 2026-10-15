class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        def backtrack(took, curr):
            if len(curr) == N:
                res.append(curr[:])
                return
            
            for i, num in enumerate(nums):
                if i in took: continue

                took.add(i)
                curr.append(num)
                backtrack(took, curr[:])

                took.remove(i)
                curr.pop()

        backtrack(set(), [])
        return res