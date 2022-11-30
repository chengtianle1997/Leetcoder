
# O(n) Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        # search from the widest container
        p, q = 0, len(height) - 1
        max_area = min(height[p], height[q]) * (q - p)
        # loop
        while p < q:
            # the smaller line cannot contain more water
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
            max_area = max(max_area, min(height[p], height[q]) * (q - p))
        return max_area
                
            
            