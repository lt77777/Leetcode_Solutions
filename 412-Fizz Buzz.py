class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtn = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                rtn.append("FizzBuzz")
                continue
            if i % 3 == 0:
                rtn.append("Fizz")
                continue
            if i % 5 == 0:
                rtn.append("Buzz")
                continue
            rtn.append(str(i))
        return rtn
