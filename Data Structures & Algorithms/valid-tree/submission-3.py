class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        visit = set()
        def dfs(i, parent):
            if i in visit: return False
            
            visit.add(i)
            for nei in hashmap[i]:
                if nei == parent: continue
                if not dfs(nei, i): return False
                
            return True

        return dfs(0, -1) and len(visit) == n