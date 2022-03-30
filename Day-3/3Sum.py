class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                low, high, a = i+1, n-1, -nums[i]
                while low < high:
                    if nums[low] + nums[high] < a:
                        low += 1
                    elif nums[low] + nums[high] > a:
                        high -= 1
                    else:
                        ans.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
        return ans
