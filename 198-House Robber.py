class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            third = max (nums[i] + first, second)
            first = second
            second = third
        return third
