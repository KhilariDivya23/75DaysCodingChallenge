class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        start, end, mid = 0, len(nums)-1, -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid] != nums[mid-1]:
                    ans[0] = mid
                    break
                else:
                    end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        start, end = mid+1, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                    if mid == len(nums)-1 or nums[mid+1] != nums[mid]:
                        ans[1] = mid
                        return ans
                    else:
                        start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        ans[1] = ans[0]
        return ans
