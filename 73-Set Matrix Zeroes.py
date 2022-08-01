class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        m_index = set()
        n_index = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_index.add(i)
                    n_index.add(j)
        for i in m_index:
            matrix[i] = [0] * n
        for j in n_index:
            for row in matrix:
                row[j] = 0
