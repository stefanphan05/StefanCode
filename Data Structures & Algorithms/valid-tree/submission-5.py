class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(cur, par):
            if cur in visit: return False

            visit.add(cur)
            for nei in adj[cur]:
                if nei == par: continue
                if not dfs(nei, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n