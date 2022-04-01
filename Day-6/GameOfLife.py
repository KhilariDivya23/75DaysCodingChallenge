class Solution:
    def curr_adj_lives(self, board, n, m, i, j):
            ans = 0
            if i-1 != -1:
                ans += board[i-1][j]
            if j-1 != -1:
                ans += board[i][j-1]
            if i-1 != -1 and j-1 != -1:
                ans += board[i-1][j-1]
            if i+1 != m:
                ans += board[i+1][j]
            if j+1 != n:
                ans += board[i][j+1]
            if i+1 != m and j+1 != n:
                ans += board[i+1][j+1]
            if i+1 != m and j-1 != -1:
                ans += board[i+1][j-1]
            if i-1 != -1 and j+1 != n:
                ans += board[i-1][j+1]
            return ans
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        new_board = [[board[i][j] for j in range(n)] for i in range(m)]
      
        for i in range(m):
            for j in range(n):
                if self.curr_adj_lives(new_board, n, m, i, j) > 3:
                    board[i][j] = 0
                elif self.curr_adj_lives(new_board, n, m, i, j) == 3:
                    board[i][j] = 1
                elif self.curr_adj_lives(new_board, n, m, i, j) < 2 and new_board[i][j] == 1:
                    board[i][j] = 0
