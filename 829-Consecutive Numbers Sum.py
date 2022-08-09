class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        while n % 2 == 0:
            # Kill even factors
            n //= 2
        result = 1
        p = 3
        while n != 1:
            count = 1
            while n % p == 0:
                n //= p
                count += 1
            result *= count
            if p**2 >= n:
                # Rest of n is prime, stop here
                if n > p:
                    # We have not counted n yet
                    result *= 2
                break
            p += 2
        return result
        
