class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key = len)
        res = ""
        for i in range(len(shortest_string)):
            char = shortest_string[i]
            for j in range(len(strs)):
                if strs[j][i] != char:
                    return res
            
            res += char
        
        return res