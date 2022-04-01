class Solution:
    def solve(self, candidates,i, n, target, ans, temp):
        if i == n and target == 0:
            ans.append([i for i in temp])
        
        if i == n:
            return  
        
        if candidates[i] <= target:
            temp.append(candidates[i])
            self.solve(candidates, i, n, target-candidates[i], ans, temp)
            if temp: temp.pop()
        self.solve(candidates, i+1, n, target, ans, temp)
                
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, temp = [], []
        self.solve(candidates, 0, len(candidates), target, ans, temp)
        return ans
