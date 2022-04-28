class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		n = len(nums)
		out = nums[0]+nums[1]+nums[2]
		nums.sort()

		for i in range(n-2):
			if (i > 0 and nums[i-1] == nums[i]):
				continue

			l = i + 1
			r = n - 1
			while(l < r):
				tmp = nums[i] + nums[l] +nums[r]
				if (abs(tmp - target) < abs(out-target)):
					out = tmp
				if (tmp < target):
					while (l+1 < r and nums[l] == nums[l+1]):
						l += 1
					l += 1
				elif (tmp > target):
					while (r-1 > l and nums[r]==nums[r-1]):
						r -= 1
					r -= 1
				else:
					return target
		return out
