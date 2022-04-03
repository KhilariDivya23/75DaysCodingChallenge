class Solution:
    def adj_land(self, i, j, m, n, grid, count):
        grid[i][j] = -1
        if i-1 > -1 and grid[i-1][j] == 1:
            count += 1
            count = self.adj_land(i-1, j, m, n, grid, count)
        if i+1 < n and grid[i+1][j] == 1:
            count += 1
            count = self.adj_land(i+1, j, m, n, grid, count)
        if j-1 > -1 and grid[i][j-1] == 1:
            count += 1
            count = self.adj_land(i, j-1, m, n, grid, count)
        if j+1 < m and grid[i][j+1] == 1:
            count += 1
            count = self.adj_land(i, j+1, m, n, grid, count)
        return count
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_land = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr_land = self.adj_land(i, j, m, n, grid, 1)
                    max_land = max(curr_land, max_land)
        return max_land
