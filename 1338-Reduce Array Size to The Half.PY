class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = math.ceil(len(arr)/2)
        freq = dict()
        for i in arr:
            if i not in freq.keys():
                freq[i] = 1
            else:
                freq[i] += 1
        vals = list(freq.values())
        vals.sort()
        vals.reverse()
        i = 0
        rtn = 0
        while target > 0 and i < len(arr):
            target -= vals[i]
            rtn += 1
            i += 1
        return rtn 
    
