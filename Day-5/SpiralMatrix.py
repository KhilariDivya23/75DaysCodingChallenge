class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, ans = len(matrix), len(matrix[0]), []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        while l < r and t < b:
            for i in range(l, r):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                ans.append(matrix[i][r-1])
            r -= 1
            if not (l < r and t < b):
                break
            i = r-1
            while i >= l:
                ans.append(matrix[b-1][i])
                i -= 1
            b -= 1
            i = b-1
            while i >= t:
                ans.append(matrix[i][l])
                i -= 1
            l += 1
        return ans
