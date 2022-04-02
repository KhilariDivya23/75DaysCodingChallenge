class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, i = 0, 0
        while i < len(nums)-1:
            goal = k+nums[i]
            if goal in nums[i+1:]:
                count += 1
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return count
