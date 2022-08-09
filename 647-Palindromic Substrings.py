class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        # index of palindromic string center
        i = 0
        while i < n:
            # k is the last index where chars from
            # i-th to k-th indexes are all the same
            k = i
            while k < n - 1 and s[k] == s[k + 1]:
                k += 1
            
            same_chars_len = k - i + 1
            # add count of palindromic string where
            # all chars are the same like: 'aaa'
            cnt += same_chars_len*(same_chars_len + 1)//2
            
            # since our center is from i-th to k-th indexes
            # try to expand around it
            left = i - 1
            right = k + 1
            while left > -1 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            
            i = k + 1

        return cnt
        
