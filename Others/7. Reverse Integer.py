
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        # deal with the minus sign
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            res = res * 10
            res += x % 10
            x = x // 10
        if sign < 0:
            res = -res
        # check boundary
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

# Consider about a 32-bit system, 2**31 will lead to a memory overflow
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MAX = 2**31
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while not x == 0:
            pop = x % 10
            x = x // 10
            # before res = res * 10 + pop, check boundary
            if res > INT_MAX / 10 or (res == INT_MAX / 10 and pop > 7):
                return 0
            res = res * 10 + pop
        if sign < 0:
            res = -res
        return res


# Convert to a string, and reverse the string
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        rev = sign * int(str(x)[::-1])
        # check boundary
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        return rev