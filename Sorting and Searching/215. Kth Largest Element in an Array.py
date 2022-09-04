from typing import List
import random

# QuickSelect, O(nlogn)
class SolutionSlow:
    def partition(self, nums, start, end):
        seperate = nums[end]
        par, itr = start, start
        while itr <= end:
            # if we find a smaller element
            if nums[itr] < seperate:
                # swap
                nums[itr], nums[par] = nums[par], nums[itr]
                par += 1
            itr += 1
        # swap the end and par
        nums[end], nums[par] = nums[par], nums[end]
        return par
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            par = self.partition(nums, start, end)
            if len(nums) - par == k:
                return nums[par]
            elif len(nums) - par > k:
                start = par + 1
            else:
                end = par - 1

# A better version of Quick Select in Python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: 
            return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M  = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
            
obj = Solution()
print(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2))


