class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        hCuts.sort()
        vCuts.sort()
        max_h, max_v, hl, vl = 0, 0, len(hCuts), len(vCuts)
        
        for i in range(hl):
            if i == 0:
                curr_h = hCuts[i]
            if i== 0 and i == hl-1:
                curr_h = max(hCuts[i], abs(hCuts[i] - h))
            elif i == hl - 1:
                curr_h = max(abs(hCuts[i] - hCuts[i-1]), abs(hCuts[i] - h))
            elif i != 0:
                curr_h = abs(hCuts[i] - hCuts[i-1])
            
            max_h = max(max_h, curr_h)
            
        for i in range(vl):
            if i == 0:
                curr_v = vCuts[i]
            if i== 0 and i == vl-1:
                curr_v = max(vCuts[i], abs(vCuts[i] - w))
            elif i == vl - 1:
                curr_v = max(abs(vCuts[i] - vCuts[i-1]), abs(vCuts[i] - w))
            elif i != 0:
                curr_v = abs(vCuts[i] - vCuts[i-1])
            
            max_v = max(max_v, curr_v)
        
        return (max_h * max_v) % (10 ** 9 + 7)
