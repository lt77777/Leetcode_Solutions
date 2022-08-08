from functools import cache


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lookup = set(words)
        
        @cache
        def dp(word):
            if word not in lookup:
                return 0
            
            return 1 + max(
                dp(word[:i] + word[i + 1:]) 
                if word[:i] + word[i + 1:] in lookup else 0
                for i in range(len(word))
            )
        
        return max(dp(word) for word in lookup)
      
