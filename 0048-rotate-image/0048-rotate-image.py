class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = left = 0
        bottom = right = len(matrix)-1
        
        while left < right:
            top = left
            bottom = right
            for i in range(right - left):
                temp = matrix[top][left + i] # store top left value
                
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            left += 1
            right -= 1