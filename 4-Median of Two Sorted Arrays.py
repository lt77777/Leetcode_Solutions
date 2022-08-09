inf = float('inf')

class Solution:
    def findMedianSortedArrays(self, l1: List[int], l2: List[int]) -> float:
        if len(l1) > len(l2):
            l1, l2 = l2, l1
        # l1 has min len
        c = (len(l2)-len(l1))//2
        L = len(l1)+len(l2)
        
        a = 0
        b = 2*len(l1)
        if len(l1) == len(l2):
            b -= 1
        
        while a <= b:
            m = (a+b)//2  # index into combined interleaving array of current candidate median
            i = m//2  # l1 index
            j = len(l2)-1 - (c + m//2)  # l2 index from back
            if m&1:  # median is in l1
                if (l2[j-1] if j > 0 else -inf) <= l1[i] <= l2[j]:  # we've found the median
                    break
                elif l1[i] > l2[j]:  # move left in l1
                    b = m-1
                else:  # l1[i] < l2[j-1]  move right in l1
                    a = m+1
            else:  # median is in l2
                if (l1[i-1] if i > 0 else -inf) <= l2[j] <= (l1[i] if i < len(l1) else inf):  # we've found the median
                    break
                elif l2[j] > (l1[i] if i < len(l1) else inf):  # move right in l1
                    a = m+1
                else:  # move left in l1
                    b = m-1
                    
        # m is the median index in the combined interleaving array
        if m&1:  # median is in l1
            med = l1[i]
            if not L&1:  # even
                med = (med + min(l2[j], l1[i+1] if i+1 < len(l1) else inf))/2
        else:
            med = l2[j]
            if not L&1:  # even
                med = (med + min(l1[i] if i < len(l1) else inf, l2[j+1] if j+1<len(l2) else inf))/2
                
        return med
        
