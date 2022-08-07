class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        for i in range(1, rowIndex+1):
            dp.append(self.getRow1(dp[-1]))
        return dp[rowIndex]
    
    def getRow1(self, preRow):
        rtn = [1]
        for i in range(len(preRow)-1):
            rtn.append(preRow[i] + preRow[i+1])
        rtn.append(1)
        return rtn
      
