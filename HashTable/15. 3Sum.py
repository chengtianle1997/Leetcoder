
# O(n^2), worst case: O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a set
        num_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in num_dict.keys():
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]] = [i]
        
        res = set()
        
        # loop
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                target = 0 - nums[i] - nums[j]
                if target in num_dict.keys():
                    for idx in num_dict[target]:
                        if not idx == i and not idx == j:
                            res.add(tuple(sorted([nums[i], nums[j], target])))
                            break
        
        return list(res)

# Two pointers Solution, sorting based
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(0, len(nums) - 2):
            # remove duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s, e = i + 1, len(nums) - 1
            while s < e:
                sum = nums[i] + nums[s] + nums[e]
                if sum < 0:
                    s += 1
                elif sum > 0:
                    e -= 1
                else:
                    # sum == 0
                    res.append([nums[i], nums[s], nums[e]])
                    # remove duplicates
                    while s < e and nums[s] == nums[s + 1]:
                        s += 1
                    while s < e and nums[e] == nums[e - 1]:
                        e -= 1
                    s += 1
                    e -= 1
                
        
        return res
                    