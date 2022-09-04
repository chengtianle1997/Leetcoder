
# O(nlogn) Solution, beat 90%+
class Solution:   
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            items = sum([bisect.bisect_right(row, mid) for row in matrix])
            if items < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

# heap n^2 logk

# sort n^2 logn