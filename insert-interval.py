class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals: list[list[int]] = []
        for index, interval in enumerate(intervals):
            interval_start, interval_end = interval[0], interval[1]
            if newInterval[1] < interval_start:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[index:])
                return new_intervals
            elif interval_end < newInterval[0]:
                new_intervals.append(interval)
            else:
                if interval_start < newInterval[0]:
                    newInterval[0] = interval_start
                if newInterval[1] < interval_end:
                    newInterval[1] = interval_end
        new_intervals.append(newInterval)
        return new_intervals
