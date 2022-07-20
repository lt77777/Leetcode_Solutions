class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        while True:
            if num * num > x:
                return num-1
                break
            num += 1
