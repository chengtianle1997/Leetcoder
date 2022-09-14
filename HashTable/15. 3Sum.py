
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

# An improved hash set solution, O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        # classify the nums into positive, negative and zero lists
        pos, neg, zeros = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                # num == 0
                zeros.append(num)
        
        # if there are more than three zeros, we will have [0, 0, 0]
        if len(zeros) >= 3:
            res.add(tuple([0, 0, 0]))
            
        # convert pos and neg to set
        pos_set, neg_set = set(pos), set(neg)
        
        # if there is at least one zeros, we can have one positive + one negative
        if len(zeros) > 0:
            for num in pos:
                target = -1 * num
                if target in neg_set:
                    res.add(tuple([target, 0, num]))
        
        # pos + pos + neg
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                target = 0 - pos[i] - pos[j]
                if target in neg_set:
                    res.add(tuple(sorted([target, pos[i], pos[j]])))
        
        # neg + neg + pos
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                target = 0 - neg[i] - neg[j]
                if target in pos_set:
                    res.add(tuple(sorted([neg[i], neg[j], target])))
        
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
                    