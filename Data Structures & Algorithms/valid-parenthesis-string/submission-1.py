class Solution:
    def checkValidString(self, s: str) -> bool:
        opens, stars = [], []

        for i, brac in enumerate(s):
            if brac == "(":
                opens.append(i)
            elif brac == "*":
                stars.append(i)
            else:                   # )
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while opens and stars:
            if opens.pop() > stars.pop():
                return False

        return not opens