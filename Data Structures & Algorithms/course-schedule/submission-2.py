class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_map = defaultdict(list)
        for a, b in prerequisites:
            prerequisites_map[a].append(b)
        
        visit = set()
        def dfs(c):
            if c not in prerequisites_map or prerequisites_map[c] == []:
                return True
            
            visit.add(c)
            for pres in prerequisites_map[c]:
                if pres in visit or not dfs(pres):
                    return False

            visit.remove(c)
            prerequisites_map[c] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
"""
0 <- 1, 2
1 <- 3
2 <- 3
3 <- 4
3 <- 5
6 <- 0
7 <- 0

visit = 0
1 -> 3 -> 4 True

2
"""