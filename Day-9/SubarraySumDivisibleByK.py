class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map, count, add = {0:1}, 0, 0
        for i in nums:
            add += i
            if add % k in hash_map:
                count += hash_map[add % k]
                hash_map[add % k] += 1
            else:
                hash_map[add % k] = 1
        return count
