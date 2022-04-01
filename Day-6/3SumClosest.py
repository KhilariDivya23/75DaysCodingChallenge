import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, max_val, dis = len(nums), 0, math.inf
        for i, j in enumerate(nums):
            l, r = i+1, n-1
            while l < r:
                add = j + nums[l] + nums[r]
                if abs(target - add) < dis:
                    dis = abs(target - add)
                    max_val = add
                if add < target:
                    l += 1
                elif add > target:
                    r -= 1
                else:
                    break
        return max_val
