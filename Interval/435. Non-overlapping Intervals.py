class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # always pick the intervals with the earliest end time
        
        # sort intervals according to the end time
        intervals.sort(key = lambda x: x[1])
        end, count = float('-inf'), 0
        # iterate
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            # if not overlaps
            if s >= end:
                end = e
            # if overlaps
            else:
                count += 1
        return count
            