class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high, area = 0, len(height)-1, 0
        while low < high:
            curr_area = (high - low) * min(height[low], height[high])
            area = max(curr_area, area)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return area
