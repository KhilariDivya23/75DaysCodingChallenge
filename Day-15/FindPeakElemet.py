class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums_dict = {j:i for i, j in enumerate(nums)}
        return nums_dict[max(nums)]
