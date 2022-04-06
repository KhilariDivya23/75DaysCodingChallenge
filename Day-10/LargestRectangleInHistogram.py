from queue import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_boundry, right_boundry = [0 for i in range(n)], [n-1 for i in range(n)]
        left_stack, right_stack = deque(), deque()
        i = 0
        while i < n:
            if left_stack:
                if heights[left_stack[-1]] >= heights[i]:
                    while left_stack and heights[left_stack[-1]] >= heights[i]:
                        left_stack.pop()
                    if left_stack:
                        left_boundry[i] = left_stack[-1]+1
                    left_stack.append(i)
                else:
                    left_stack.append(i)
                    left_boundry[i] = i
            else:
                left_stack.append(i)
            i += 1
        
        i = n-1
        while i >= 0:
            if right_stack:
                if heights[right_stack[-1]] >= heights[i]:
                    while right_stack and heights[right_stack[-1]] >= heights[i]:
                        right_stack.pop()
                    if right_stack:
                        right_boundry[i] = right_stack[-1]-1
                    right_stack.append(i)
                else:
                    right_stack.append(i)
                    right_boundry[i] = i
            else:
                right_stack.append(i)
            i -= 1
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right_boundry[i]-left_boundry[i]+1)*heights[i])
        return max_area
