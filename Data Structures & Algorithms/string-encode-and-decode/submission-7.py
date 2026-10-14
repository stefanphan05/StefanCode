class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += "|" + str(len(string)) + "|" + string
        
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        print(len(s))
        res = []
        i = 0
        while i + 1 < len(s):

            j = i + 1
            while s[j] != "|":
                j += 1

            length = int(s[i + 1:j])
            print(i, s[i], length)
            
            start_index = i + 2 + len(s[i + 1: j])
            end_index = start_index + length
            res.append(s[start_index:end_index])

            i = end_index

        return res

"""
"Hello","World5", "5Guys"
|5|Hello|6|World5|5|5Guys
012345678

|5|Hello5World555Guys

Hello, World

s|10|!@#$%^&*()
0123456789
"""