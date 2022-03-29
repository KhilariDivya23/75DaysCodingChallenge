class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, add, map_dict = 0, 0, {0:1}
        for i in nums:
            add += i
            if add-k in map_dict:
                count += map_dict[add-k]
            if add in map_dict:
                map_dict[add] += 1
            else:
                map_dict[add] = 1
        return count
