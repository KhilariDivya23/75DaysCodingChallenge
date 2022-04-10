class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end, n = 0, len(nums)- 1, len(nums)
        while start <= end:
            mid = (start + end) // 2
            if mid == 0 and end == 1:
                if nums[mid] > nums[end]:
                    return mid
                return end
            elif mid == 0 or mid == n - 1:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid -1]:
                start = mid + 1
            else:
                end = mid - 1    
