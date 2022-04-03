class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r, l = 0, 0
        while r < len(nums)-1:
            max_dis = 0
            for i in range(l, r+1):
                max_dis = max(max_dis, i+nums[i])
            l, r = r+1, max_dis
            if max_dis == 0:
                return False
        return True
