class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        word_dict_set = set(wordDict)
        memo = {}
        
        def dfs(i, last_start):
            state = (i, last_start)
            if state in memo:
                return memo[state]
            if i >= N:
                if s[last_start:] in word_dict_set:
                    return True
                return False
            
            # Split here
            if s[last_start: i + 1] in word_dict_set and dfs(i + 1, i + 1):
                memo[state] = True
                return True

            # Nope keep going
            if dfs(i + 1, last_start):
                memo[state] = True
                return True
            
            memo[state] = False
            return False
        
        return dfs(0, 0)