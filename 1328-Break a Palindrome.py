class Solution:
    def breakPalindrome(self, p: str) -> str:
        if(len(p) == 1):
            return  ""
        n = len(p)
        p = list(p)
        for i in range(n//2):
            if(p[i] != 'a'):
                p[i] = "a"
                return "".join(p)
        p[-1] = "b"
        return "".join(p)
        
