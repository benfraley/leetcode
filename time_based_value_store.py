# https://neetcode.io/problems/time-based-key-value-store
class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = {}
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        time = 0
        if key in self.values:
            for (k, v) in self.values[key].items():
                if k <= timestamp and k > time:
                    ret = v
                    time = k
        return ret
