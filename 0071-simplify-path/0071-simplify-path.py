class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path_list = path.split("/")
        for p in path_list:
            if p:
                if p == "..":
                    if res:
                        res.pop()
                elif p == '.':
                    continue
                else:
                    res.append(p)
        res = "/" + "/".join(res)
        return res
        