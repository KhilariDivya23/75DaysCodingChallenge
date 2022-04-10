class Solution:
    def myPow(self, x: float, no: int) -> float:
        ans, n = 1, abs(no)
        while n != 0:
            if n % 2 == 0:
                x, n = x*x, n / 2
            else:
                ans *= x
                n -= 1
        if no < 0:
            ans = 1 / ans
        return ans
