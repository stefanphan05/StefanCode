class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        hashmap = defaultdict(list)
        for a, b in prerequisites:
            hashmap[a].append(b)
        
        visit = set()
        done = set()
        def dfs(c):
            if c in visit: return False
            if c in done: return True
 
            visit.add(c)
            for pre in hashmap[c]:
                if not dfs(pre): return False
            
            visit.remove(c)
            done.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return res if len(res) == numCourses else []

"""
0 <- 1
1 <- 2
2 <- 0
"""