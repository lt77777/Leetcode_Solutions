class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        
        while True:
            for i in alphabet:
                if i in d and d[i] > 0:
                    d[i] -= 1
                    result += i
            for j in reversed(alphabet):
                if j in d and d[j] > 0:
                    d[j] -= 1
                    result += j
            if sum(v for k,v in d.items())==0:
                break
        return result 
    
