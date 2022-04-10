class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n, count = len(grid[0]), len(grid), 0
        for row in grid:
            start, end = 0, m - 1
            while start <= end:
                mid = (start + end) // 2
                if row[mid] < 0:
                    if mid == 0 or row[mid-1] >= 0:
                        count += m-mid
                        break                        
                    else:
                        end = mid - 1
                else:
                    start = mid + 1
        return count
