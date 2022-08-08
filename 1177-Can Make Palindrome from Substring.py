class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        d = defaultdict(int)
        count = [None]*n
        for i in range(n):
            d[s[i]] += 1
            count[i] = d.copy()
        def check(start,end,k):
            prev = defaultdict(int) if start == 0 else count[start-1]
            left = 0
            for i in range(26):
                diff = (count[end][chr(i+97)] - prev[chr(i+97)]) % 2
                if diff == 1: left += 1
            left = left // 2
            return left <= k
        ans = []
        for start,end,k in queries:
            ans.append(check(start,end,k))
        return ans
      
