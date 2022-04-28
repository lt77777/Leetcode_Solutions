class Solution(object):
    def case_zero(self,nums, index):
        for i in range(1, index + 1):
            if nums[index - i] > i:
                return True
        return False
    def case_zero_end(self,nums, index):
        for i in range(1, index + 1):
            if nums[index - i] >= i:
                return True
        return False
    def canJump(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if len(nums) == 2:
            if nums[0] > 0:
                return True
        for i in range(len(nums)):
            if nums[i] == 0 and i == len(nums) - 1:
                if not self.case_zero_end(nums, i):
                    return self.case_zero_end(nums, i)
                break
            if nums[i] == 0:
                if not self.case_zero(nums, i):
                    return self.case_zero(nums, i)
        return True
