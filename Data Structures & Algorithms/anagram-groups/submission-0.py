class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            lst = [0] * 26

            for char in string:
                index = ord(char) - ord("a")
                lst[index] += 1

            tuple_list = tuple(lst)
            if tuple_list in hashmap:
                hashmap[tuple_list].append(string)
            else:
                hashmap[tuple_list] = [string]
    
        return list(hashmap.values())

"""
["act","pots","tops","cat","stop","hat"]
n x mlogm
n

[
"act", "act"

"act", "cat"
]

hashmap
"act" -> ["act", "cat"]

return hashmap.values()

tuple(1, 0, 1..., 1)
"""