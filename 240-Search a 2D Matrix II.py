class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        z=[]
        for ele in matrix:
            for bele in ele:
                if bele==target:
                    return True
        return False
      
