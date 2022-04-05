class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        min_index = -1
        while i < len(nums):
            if nums[i] <= 0:
                i += 1
            elif (i == 0 or nums[i-1] <= 0) and nums[i] != 1:
                return 1
            else:
                min_no, min_index = nums[i], i
                break
        if min_index == -1:
            return 1
        for i in range(min_index+1, len(nums)):
            if nums[i] == min_no or nums[i] == min_no+1:
                min_no = nums[i]
            else:
                return min_no + 1
        return min_no+1
