class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        hours_taken = sum(piles)
        while hours_taken > h:
            k *= 2
            hours_taken = sum([math.ceil(p / k) for p in piles])
        if k == 1:
            return k

        l = k/2
        while l < k:
            mid = (l + k) // 2
            val = sum([math.ceil(p / mid) for p in piles])

            if val <= h:
                k = mid
            else:
                l = mid + 1
        return int(k)
      
