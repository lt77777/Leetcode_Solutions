class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if leng == 1:
            return 0
        dp = [0] * leng
        nums[-1] = 0
        for i in range(leng - 2, -1, -1):
            if nums[i] == 0:
                nums[i] = 10001
                continue
            temp = nums[i + 1:i+nums[i] + 1]
            nums[i] = 1 + min(temp)
        return nums[0]
            
