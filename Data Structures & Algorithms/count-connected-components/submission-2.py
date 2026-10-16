class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set()
        count = 0
        for num in range(n):
            nodes.add(num)

        hashmap = defaultdict(list)
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        def dfs(curr, parent, visit):
            if curr in visit: return
            if curr in nodes:
                nodes.remove(curr)
            visit.add(curr)
            for nei in hashmap[curr]:
                if nei == parent: continue
                dfs(nei, curr, visit)
        
        while nodes:
            count += 1
            node = nodes.pop()
            dfs(node, -1, set())

        return count