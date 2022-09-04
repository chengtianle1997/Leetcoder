from typing import List

# Log N solution
class SolutionLogN:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # mid and target on the same side
            if (nums[mid] - nums[-1]) * (target - nums[-1]) > 0:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            # not on the same side, but target on the left side
            elif target > nums[-1]:
                hi = mid
            # target is on the right side
            else:
                lo = mid + 1
        if nums[lo] == target:
            return lo
        else:
            return -1

# N + log(N)
class Solution:
    def ori2sort(self, idx):
        return (idx - self.pivot) % self.len
    
    def sort2ori(self, idx):
        return (idx + self.pivot) % self.len
    
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot
        self.pivot = 0
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    self.pivot = i
                    break
        self.len = len(nums)
        
        # binary search, lo, hi are pointers for the sorted array
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[self.sort2ori(mid)] < target:
                lo = mid + 1
            elif nums[self.sort2ori(mid)] > target:
                hi = mid
            else:
                return self.sort2ori(mid)
        return -1
        
        
        
            
obj = Solution()
#print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))
print(obj.search([1], 1))