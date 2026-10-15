class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        lst = self.hashmap[key]
        l, r = 0, len(lst) - 1
        max_time, max_m = -1, -1
        while l <= r:
            m = (l + r) // 2
            if lst[m][0] <= timestamp:
                max_time = max(lst[m][0], max_time)
                max_m = m
                l = m + 1
            else:
                r = m - 1
        
        if max_time == -1:
            return ""
        
        return lst[max_m][1]

"""


alice -> 1 -> happy
      -> 3 -> sad
"""