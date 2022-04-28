from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = defaultdict(int)
        seen1 = set()
        for i in range(len(nums)):
            if target - nums[i] in seen1:
                return [i, seen[target - nums[i]]]
            seen1.add(nums[i])
            seen[nums[i]] = i
        
