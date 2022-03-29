class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, nums), key=lambda x: abs(x))
