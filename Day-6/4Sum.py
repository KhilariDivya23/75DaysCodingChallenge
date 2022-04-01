class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                for j in range(i+1,n):
                    if j > i+1 and nums[j] == nums[j-1]:
                        continue
                    else:
                        l, r = j+1, n-1
                        t = target - (nums[i] + nums[j])
                        while l < r:
                            add = nums[l] + nums[r]
                            if add == t:
                                ans.append((nums[i], nums[j], nums[l], nums[r]))
                                while l<r and nums[l] == nums[l+1]:
                                    l += 1
                                while l< r and nums[r] == nums[r-1]:
                                    r -= 1
                                l += 1
                                r -= 1
                            elif add < t:
                                l += 1
                            else:
                                r -= 1
        return ans
