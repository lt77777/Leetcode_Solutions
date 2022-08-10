class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		s2 = 0
		s1 = 0
		b1 = -math.inf
		b2 = -math.inf

		for p in prices:
			s2 = max(s2,p+b2)
			b2 = max(b2,s1-p)
			s1 = max(s1,p+b1)
			b1 = max(b1,-p)

		return s2
    
