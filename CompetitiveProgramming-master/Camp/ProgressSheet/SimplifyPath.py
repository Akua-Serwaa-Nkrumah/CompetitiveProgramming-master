class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue

            j = i
            filename = ""
            while j < len(path) and path[j] != '/':
                filename += path[j]
                j += 1

            i = j

            if filename == '.':
                continue

            if filename == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(filename)
        
        return "/" + "/".join(stack)

        