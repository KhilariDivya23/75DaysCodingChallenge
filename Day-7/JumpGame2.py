class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, l, r = 0, 0, 0
        while r < len(nums) - 1:
            max_distance = 0
            for i in range(l,r+1):
                max_distance = max(max_distance, i+nums[i])
            l = r+1
            r = max_distance
            jumps += 1
        return jumps
