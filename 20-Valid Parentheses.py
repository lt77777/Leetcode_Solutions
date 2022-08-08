class Solution:
    def isValid(self, s: str) -> bool:
        valid = dict([["(",")"], ["{","}"], ["[","]"]])
        stack = []
        for i in s:
            if i in valid.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if i != valid[curr]:
                    return False
        return len(stack) == 0
