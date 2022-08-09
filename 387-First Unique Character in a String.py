class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(list(s))
        for char in s:
            if char in c and c[char] == 1:
                return s.find(char)
        return -1
    
