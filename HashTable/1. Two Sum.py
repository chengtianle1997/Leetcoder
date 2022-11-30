# O(N) Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in num_dict.keys():
                return [i, num_dict[another]]
            else:
                num_dict[nums[i]] = i
                