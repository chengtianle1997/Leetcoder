from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs_left(val, t, lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if val[mid] < target:
                    # search right
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo
            
        def bs_right(val, t, lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if val[mid] <= target:
                    # search right
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi
        
        lo = bs_left(nums, target, 0, len(nums) - 1)
        hi = bs_right(nums, target, 0, len(nums) - 1)
        return [lo, hi] if lo <= hi else [-1, -1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findIndex(nums, target, leftBias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    # search left
                    right = mid - 1
                elif nums[mid] < target:
                    # search right
                    left = mid + 1
                else:
                    # nums[mid] == target
                    if leftBias:
                        i = mid
                        right = mid - 1
                    else:
                        i = mid
                        left = mid + 1
            return i
        
        left_idx, right_idx = findIndex(nums, target, True), findIndex(nums, target, False)
        return [left_idx, right_idx]
            

obj = Solution()
print(obj.searchRange([5, 7, 7, 8, 8, 10], 6))