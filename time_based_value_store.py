# https://neetcode.io/problems/time-based-key-value-store
class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        if key in self.values:
            l, r = 0, len(self.values[key]) - 1
            while l <= r:
                m = (l+r) // 2
                if self.values[key][m][0] == timestamp:
                    ret = self.values[key][m][1]
                    break
                elif self.values[key][m][0] < timestamp:
                    ret = self.values[key][m][1]
                    l = m + 1
                else:
                    r = m - 1
        return ret
