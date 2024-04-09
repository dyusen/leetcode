class TimeMap:

    def __init__(self):
        """
        storage = {
            "foo": [
                [2, "bar"],
                [4,"bar2"],
                [8,"bar3"],
                [16,"bar4"],
            ]
        }

        """
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key].append([timestamp, value])
        else:
            self.storage[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        value_array = self.storage.get(key)
        if not value_array:
            return ""
        if timestamp > value_array[-1][0]:
            return value_array[-1][1]

        l = 0
        r = len(value_array)
        while l <= r:
            mid = (l + r) // 2
            if value_array[mid][0] > timestamp:
                r = mid - 1
            elif value_array[mid][0] <= timestamp:
                if (len(value_array) - 1 > mid and value_array[mid + 1][0] > timestamp) or value_array[mid][
                    0] == timestamp:
                    return value_array[mid][1]
                else:
                    l = mid + 1
        return ""
