class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = 0
        i = 0
        try:
            while i < len(s):
                curr = s[i]
                if curr == 'M':
                    rtn += 1000
                    i += 1
                    continue
                if curr == 'D':
                    rtn += 500
                    i += 1
                    continue
                if curr == 'C':
                    rtn += 100
                    if s[i+1] == 'M':
                        rtn += 800
                        i += 2
                        continue
                    if s[i+1] == 'D':
                        rtn += 300
                        i += 2
                        continue
                    i += 1
                    continue
                if curr == 'L':
                    rtn += 50
                    i += 1
                    continue
                if curr == 'X':
                    rtn += 10
                    if s[i+1] == 'C':
                        rtn += 80
                        i += 2
                        continue
                    if s[i+1] == 'L':
                        rtn += 30
                        i += 2
                        continue
                    i += 1
                    continue
                if curr == 'V':
                    rtn += 5
                    i += 1
                    continue
                if curr == 'I':
                    rtn += 1
                    if s[i+1] == 'X':
                        rtn += 8
                        i += 2
                        continue
                    if s[i+1] == 'V':
                        rtn += 3
                        i += 2
                        continue
                    i += 1
                    continue
        except IndexError:
            return rtn
        return rtn
