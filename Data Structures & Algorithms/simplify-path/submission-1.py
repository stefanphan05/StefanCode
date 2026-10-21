class Solution:
    def simplifyPath(self, path: str) -> str:
        path_lst = path.split("/")
        stack = []

        for pa in path_lst:
            if not pa: continue
            if pa == "..":
                if stack: 
                    stack.pop()
            elif pa == ".":
                continue
            else:
                stack.append(pa)

        return "/" + "/".join(stack)