from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result, ts_values = "", self.table[key]

        low, high = 0, len(ts_values) - 1
        while low <= high:
            mid = (low + high) // 2
            ts, value = ts_values[mid]

            if ts <= timestamp:
                result = value
                low = mid + 1

            else:
                high = mid - 1

        return result
