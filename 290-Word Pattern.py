from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_split = s.split(" ")
        mappings = defaultdict()
        pattern_len = len(pattern)
        if len(s_split) % pattern_len != 0:
            return False
        i = 0
        while i < len(s_split):
            j = 0
            while j < pattern_len and i + j < len(s_split):
                if pattern[j] in mappings.keys():
                    if s_split[i + j] != mappings[pattern[j]]:
                        return False
                else:
                    if s_split[i+j] in mappings.values():
                        return False
                    else:
                        mappings[pattern[j]] = s_split[i+j]
                j += 1
            i += pattern_len
        return True
