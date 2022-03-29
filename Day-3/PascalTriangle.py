class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if  i > 1 and 0 < j < i:
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
