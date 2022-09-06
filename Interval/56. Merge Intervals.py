

# O(nlogn + n) Solution with Sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if len(intervals) == 0:
            return merged
        
        # sort the intervals
        intervals.sort(key = lambda x: x[0])
        
        merged.append(intervals[0])
        prev = merged[0]
        
        for i in range(1, len(intervals)):
            cur = intervals[i]
            
            # check overlapping
            if prev[1] >= cur[0]:
                # merge
                prev[1] = max(cur[1], prev[1])
            else:
                merged.append(cur)
            
            prev = merged[-1]
        
        return merged


# O(nˆ2) Solution
class Solution:
    def overlap(self, a, b):
        if a[0] <= b[1] and b[0] <= a[1]:
            return True
        else:
            return False
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        if len(intervals) == 0:
            return merged
        merged.append(intervals[0])
        
        for interval in intervals:
            idx = 0
            while idx < len(merged):
                merge = merged[idx]
                # check overlapping
                if self.overlap(interval, merge):
                    # we find the first overlapping interval,
                    # pop out the merge, and update the interval to a merged one
                    del merged[idx]
                    interval = [min(interval[0], merge[0]), max(interval[1], merge[1])]
                else:
                    idx += 1
            # append the interval
            merged.append(interval)
        
        return merged
                    