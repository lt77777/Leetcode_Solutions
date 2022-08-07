class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        best = []
        for j in range(len(strs[0])):
            try:
                if strs[0][j] == strs[1][j]:
                    best.append(strs[0][j])
                else:
                    break
            except IndexError:
                break
        if len(strs) == 2:
            return "".join(best)
        for i in range(2, len(strs)):
            curr = []
            for j in range(len(strs[i])):
                try:
                    if strs[i][j] == best[j]:
                        curr.append(best[j])
                    else:
                        break
                except IndexError:
                    break
            best = curr
        return "".join(best)
