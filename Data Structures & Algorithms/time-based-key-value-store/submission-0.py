class TimeMap:

    def __init__(self):
        self.t_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = []
        self.t_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.t_map:
            return ""

        values_list = self.t_map[key]
        best_answer = ""
        low = 0
        high = len(values_list) - 1

        while low <= high:

            mid = (low + high) // 2
            cur_timestamp, cur_value = values_list[mid]

            if cur_timestamp <= timestamp:
                best_answer = cur_value
                low = mid + 1
            else:
                high = mid - 1

        return best_answer

        

