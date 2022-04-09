class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)-1
        while start <= end:
            mid = (start + end) // 2
            if mid == 0:
                return 1
            if arr[mid] > arr[mid-1]:
                start = mid + 1
            elif arr[mid] < arr[mid-1]:
                end = mid - 1
        return end
