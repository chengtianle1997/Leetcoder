
# O(N^2) Solution, memorization, Beat 20%
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # if there is a longer subsequence, update it
                    res[i] = max(res[i], 1 + res[j])
        return max(res)

# O(NlogN) Solution, Beat 75%+
# Only the last item of the subsequence count, 
# we can replace the elements in the middle without changing the length.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []    
        # iterate through the sequence
        for i in range(len(nums)):
            # check if the sub-sequence can be extended
            if len(sub) == 0 or nums[i] > sub[len(sub) - 1]:
                sub.append(nums[i])
            # else, replace it
            else:
                # find the insert position with binary search
                lo, hi = 0, len(sub) - 1
                mid = int((lo + hi) / 2)
                while lo <= hi:
                    if sub[mid] > nums[i]:
                        hi = mid - 1
                    elif sub[mid] < nums[i]:
                        lo = mid + 1
                    else:
                        lo = mid
                        break
                    mid = int((lo + hi) / 2)
                sub[lo] = nums[i]
        return len(sub)