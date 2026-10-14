class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += "|" + str(len(string)) + "|" + string
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "|":
                j += 1

            num = int(s[i + 1:j])
            
            start_index = i + 2 + len(str(num))
            end_index = start_index + num
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