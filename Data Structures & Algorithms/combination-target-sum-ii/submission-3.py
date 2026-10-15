class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        N = len(candidates)

        def backtrack(i, total, path):
            if i >= N or total >= target:
                if total == target:
                    res.append(path[:])
                return
            
            num = candidates[i]
            path.append(num)
            backtrack(i + 1, total + num, path[:])
            path.pop()

            while i < N - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, total, path[:])

        backtrack(0, 0, [])
        return res