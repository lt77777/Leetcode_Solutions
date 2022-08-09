class Solution:
    def isHappy(self, n: int) -> bool:
        
        newn = list(str(n))     # convert n to a list of strings
        save = []
        total = 0
        
        while total != 1:       # while total is not 1, iterate through newn, total += int(newn[i]) ** 2, convert total to a list of strings, then if the number = 1, return True. else if the number is in save return False because it will just repeat the process again. or else append the number to save.
            total = 0
            for i in range(len(newn)):
                total += int(newn[i]) ** 2
            newn = list(str(total))
            
            if int(''.join(newn)) == 1:
                return True
            
            else:
                if int(''.join(newn)) in save:
                    return False
                else:
                    save.append(int(''.join(newn)))
