class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while left < right and top < bottom:
            
            # add values left --> right
            for i in range(left, right):
                output.append(matrix[top][i])
            # done with this top row, we increment top
            top += 1
            
            # add values top --> bottom
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            # done with right column, decrement right
            right -= 1
            
            
            if not (left < right and top < bottom):
                break
                
            # add values right --> left
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            
            # done with bottom row, we decrement bottom
            bottom -= 1
            
            # add values bottom --> top
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            
            # done with left row, we increment left
            left += 1
            
        return output
        