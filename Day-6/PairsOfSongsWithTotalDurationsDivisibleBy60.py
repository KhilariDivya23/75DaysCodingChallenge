class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem, count =[], 0
        for i in range(len(time)):
            rem.append(time[i] % 60)
        hash_map = {}
        for i in rem:
            if i == 0 and i in hash_map:
                count += hash_map[i]
            elif 60-i in hash_map:
                count += hash_map[60-i]
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        return count
