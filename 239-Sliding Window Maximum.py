class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l, r = 0, 0
        ans = []
        q = collections.deque()  # deque of index
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if q[0] < l:  # no longer in the window
                q.popleft()
            
            if r + 1 >= k:  # if window has formed
                ans.append(nums[q[0]])
                l += 1
            r += 1
        return ans
    
