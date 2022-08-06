class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        amt = math.floor(len(nums)/3)
        rtn = []
        freq = dict()
        for i in nums:
            if i not in freq.keys():
                freq[i] = 1
            else:
                freq[i] += 1
        for i in list(set(nums)):
            if freq[i] > amt:
                rtn.append(i)
        return rtn
            
