class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif mid == 0 and nums[end] != target:
                return -1
            elif mid == len(nums)-1 and nums[start] != target:
                return -1
            elif nums[start] <= nums[mid]:
                if target in range(nums[start],nums[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[end] >= nums[mid]:
                if target in range(nums[mid], nums[end]) or nums[end] == target:
                    start = mid + 1
                elif start <= end:
                    end = mid - 1
        return -1
