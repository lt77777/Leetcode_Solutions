class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        rtn = 0
        ind = -1
        prev_ind = 0
        temp = []
        # temp.append(s[0])
        for i in range(len(s)):
            if s[i] in temp:
                tem = s[:i]
                tem.reverse()
                ind = tem.index(s[i])
                temp = s[i - ind:i + 1]
                continue
            temp.append(s[i])
            if len(temp) > rtn:
                rtn = len(temp)
        return rtn
