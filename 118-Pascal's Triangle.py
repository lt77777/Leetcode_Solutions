class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            dp.append(self.getRow(dp[-1]))
        return dp
    def getRow(self, preRow):
        rtn = [1]
        for i in range(len(preRow)-1):
            rtn.append(preRow[i] + preRow[i+1])
        rtn.append(1)
        return rtn
