class TimeMap:
    def __init__(self):
        self.map = {} # string -> []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map[key]
        # to improve runtime, we can also do a binayr search here
        for i in range(len(values)-1, -1, -1):
            val, t = values[i]
            if t <= timestamp:
                return val
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)