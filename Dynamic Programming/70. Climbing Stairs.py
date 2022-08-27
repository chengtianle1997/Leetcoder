
# Recursion, Time Limit Error
class Solution:    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Bottom-Up, beat 50%+
class Solution:    
    def climbStairs(self, n: int) -> int:
        # corner cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        # res[n] is the result for input n
        res = [0] * (n + 1)
        res[1], res[2] = 1, 2
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]

# Bottom-Up, constant space
class Solution:    
    def climbStairs(self, n: int) -> int:
        # corner cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        # res[n] is the result for input n
        res_ppre, res_pre = 1, 2
        for i in range(3, n + 1):
            res_cur = res_pre + res_ppre
            # update pre and ppre
            res_ppre = res_pre
            res_pre = res_cur
        return res_pre
