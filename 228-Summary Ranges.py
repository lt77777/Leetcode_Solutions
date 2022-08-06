class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        rtn = []
        while i < len(nums):
            curr = nums[i]
            try:
                while nums[i] == nums[i+1] - 1:
                    i += 1
            except IndexError:
                pass
            if nums[i] == curr:
                rtn.append(str(curr))
            else:
                rtn.append(str(curr) + "->" + str(nums[i]))
            i += 1
        return rtn
