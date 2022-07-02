class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_digits = len(num1)
        num_1 = 0
        for i in range(num1_digits):
            num_1 += (int(num1[i]) * 10**(num1_digits - 1 - i))
        num2_digits = len(num2)
        num_2 = 0
        for j in range(num2_digits):
            num_2 += (int(num2[j]) * 10**(num2_digits - 1 - j))
        return str(num_1 * num_2)
            
