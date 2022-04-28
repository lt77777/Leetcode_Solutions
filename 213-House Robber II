class Solution(object):
    def rob1(self, nums1):
        res = [0] * len(nums1)
        res[0] = nums1[0]
        res[1] = nums1[1]
        res[2] = max(nums1[0]+nums1[2], nums1[1])
        for i in range(3, len(nums1)):
            res[i] = max(res[i-2]+nums1[i], res[i-3]+nums1[i])
        return max(res)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_houses = len(nums)
        if num_houses < 4:
            return max(nums)
        if num_houses == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
    
    
