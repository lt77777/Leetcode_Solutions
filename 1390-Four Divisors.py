class Solution:
     def sumFourDivisors(self, nums: List[int]) -> int:
        sum_divisor = 0 
        for num in nums:
            x = int(math.sqrt(num))
            count = 0 #Keeping count since exactly 4 factors are needed
            total = 0 #keeping track of sum of factors for that number
            for i in range(1,x+1):
                if num%i==0:
                    if i*i==num:
                        count = -1
                        break
                    else:
                        total+=i
                        total+=num//i
                        count+=2
            if count==4: #if there are exactly 4 factors
                sum_divisor+=total #we add the sum of factors to the main sum
        return sum_divisor
