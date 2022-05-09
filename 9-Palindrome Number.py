class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 1
        while x[i-1] == x[-i] and i < len(x):
            i += 1
        if i == len(x):
            return True
        else:
            return False
