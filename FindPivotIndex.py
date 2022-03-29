class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if (i == 0 and sum(nums[i+1:]) == 0) or (i == n-1 and sum(nums[:i]) == 0):
                return i
            elif sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
        
