# Find the Pivot and Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        if len(nums) == 1:
            return nums[0] == target
        
        # find pivot
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
        
        
        # make sure which part does target belong to
        n = len(nums)
        k = min(i + 1, n - 1)
        lo, hi = 0, n - 1
        if target >= nums[0] and target <= nums[i]:
            lo, hi = 0, i
        elif target <= nums[n - 1] and target >= nums[k]:
            lo, hi = k, n - 1
        else:
            return False

        
        # binary search
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return True
        
        return False


# Revised Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] >= nums[start]:
                    if target >= nums[start] and target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if target > nums[mid] and target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
            
        return -1
                    