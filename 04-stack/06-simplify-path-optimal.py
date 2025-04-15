class Solution:
    def simplifyPath(self, path):
        stack = []
        components = path.split("/")
        
        for i, component in enumerate(components):
            if component == "" or component == ".":
                continue
            if component == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(component)
        
        if not stack:
            return "/"
        
        res = ""
        while stack:
            res = "/" + stack.pop() + res
        
        return res