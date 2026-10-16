class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        hashmap = defaultdict(list)
        for a, b in prerequisites:
            hashmap[a].append(b)
        
        visit = set()
        def dfs(c):
            if c in visit: return False
            if c not in hashmap or hashmap[c] == []: 
                if c not in res:
                    res.append(c)
                return True
            visit.add(c)
            for pre in hashmap[c]:
                if pre in visit or not dfs(pre): return False
            
            visit.remove(c)
            res.append(c)
            hashmap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return res if len(res) == numCourses else []

"""
0 <- 1
1 <- 2
2 <- 0
"""