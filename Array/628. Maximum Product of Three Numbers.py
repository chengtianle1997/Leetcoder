class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # sort the sequence
        nums.sort()
        
        # all positive or all negative
        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-3] * nums[-2] * nums[-1]
        
        # positive and negatives
        max_3 = nums[-3] * nums[-2] * nums[-1]
        max_1_min_2 = nums[-1] * nums[0] * nums[1]
        
        return max(max_3, max_1_min_2)