class Solution:     
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans, i = [intervals[0]], 1
        while i < len(intervals):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
            i += 1
        return ans
