class TimeMap:

    def __init__(self):
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append([value, timestamp])
        else:
            self.hash_map[key] = [[value, timestamp]]            
        

    def get(self, key: str, timestamp: int) -> str:
        ans, flag = "", 0
        if key in self.hash_map:
            start, end = 0, len(self.hash_map[key])-1
            while start <= end:
                mid = (start + end) // 2
                if self.hash_map[key][mid][1] == timestamp:
                    ans = self.hash_map[key][mid][0]
                    flag = 1
                    break
                elif self.hash_map[key][mid][1] > timestamp:
                    end = mid -1
                else:
                    start = mid + 1
            if end != -1 and flag == 0:
                ans = self.hash_map[key][end][0]
        return ans
