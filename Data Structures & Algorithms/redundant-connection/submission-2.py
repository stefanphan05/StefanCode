class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  
        
        
        def detect_cycle(curr, parent):
            if curr in visit: return True
            
            visit.add(curr)
            for nei in hashmap[curr]:
                if nei == parent: continue
                if detect_cycle(nei, curr): return True
            
            return False
        
        hashmap = defaultdict(list)
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
            visit = set()
            
            if detect_cycle(a, -1):
                return [a, b]
