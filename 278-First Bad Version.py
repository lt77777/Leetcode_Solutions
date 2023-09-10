# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        r=n-1
        mi=n
        while l<=r:
            mid=(l+r)>>1
            if isBadVersion(mid)==True:
                r=mid-1
                mi=min(mi, mid)
            else:
                l=mid+1         
        return mi
      
