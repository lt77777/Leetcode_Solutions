class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, ans, product = 0, 0, 1
        for r in range(len(nums)):
            product *= nums[r]
            if product < k:
                ans += r-l+1
            else:
                while l <= r and product >= k:
                    product = product / nums[l]
                    l += 1
                ans += r-l+1
        return ans
    
