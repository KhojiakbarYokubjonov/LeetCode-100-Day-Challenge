class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        belowRow = [1] * n
        for j in range(m-2, -1, -1):
            currentRow = [1] * n
            for i in range(n-2, -1, -1):
                currentRow[i] = currentRow[i+1] + belowRow[i]
            belowRow = currentRow
            
        # print(belowRow)
        return belowRow[0]
        