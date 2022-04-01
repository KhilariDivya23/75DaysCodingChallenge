class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_arr, add, n = [], 0, len(cardPoints)
        for i in cardPoints:
            add += i
            sum_arr.append(add)
        
        limit, max_val, curr_val, pts = n - k, 0, 0, sum(cardPoints)
        for i in range(n-limit+1):
            if i == 0:
                curr_val = sum_arr[i-1+limit]
            else:
                curr_val = sum_arr[i-1+limit] - sum_arr[i-1]
            max_val = max(max_val, pts - curr_val)
        return max_val
