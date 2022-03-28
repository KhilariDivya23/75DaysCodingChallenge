class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for pos, value in enumerate(nums):
            find = target - value
            if find in nums[pos+1:]:
                nums[pos] = ''
                return [pos, nums.index(find)]
