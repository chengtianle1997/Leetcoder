
# Solution with stack (Beat 30%+)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0 for idx in range(len(temperatures))]
        stack = []
        # push in the last index
        stack.append(len(temperatures) - 1)
        # iterate backwards
        for p in range(len(temperatures) - 2, -1, -1):
            while len(stack) > 0 and temperatures[p] >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                ret[p] = stack[-1] - p
            stack.append(p)
        return ret

# A better solution refer to the previous results (Beat 90%+)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        right_max = len(temperatures) - 1
        for i in range(len(temperatures) - 2, -1, -1):
            # if the temp is higher than right_max, it means there is no warmer temp afterwards
            if temperatures[i] >= temperatures[right_max]:
                # update the right_max
                right_max = i
            else:
                d = 1
                while temperatures[i] >= temperatures[i + d]:
                    # refer to the existing next warmer day
                    d += ret[i + d]
                ret[i] = d
        return ret

                