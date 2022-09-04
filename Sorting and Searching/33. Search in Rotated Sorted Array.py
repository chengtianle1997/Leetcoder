class Solution:
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
            