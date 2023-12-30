class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height)
        
        for i in range(len(heights)):
            h = heights[i]
            start = i
            
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                area = height * (i - ind)
                max_area = max(max_area, area)
                start = ind
            
            stack.append((start, h))
            
        for index, height in stack:
            max_area = max(max_area, (len(heights) - index) * height)
        return max_area
        