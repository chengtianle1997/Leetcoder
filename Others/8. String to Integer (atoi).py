class Solution:
    def myAtoi(self, s: str) -> int:
        
        INT_MAX = 2**31
        
        if len(s) == 0:
            return 0
        idx = 0
        
        # delete leading whitespace
        while idx < len(s) and s[idx] == ' ':
            idx += 1
            
        if idx >= len(s):
            return 0
        
        # read in the sign
        sign = 1
        if s[idx] in ['-', '+']:
            sign = -1 if s[idx] == '-' else 1
            idx += 1
        
        # read in the digits
        res = 0
        while idx < len(s) and s[idx].isdigit():
            pop = int(s[idx])
            # check bound
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                return 2**31 - 1 if sign > 0 else -2**31
            res = res * 10 + pop
            idx += 1
        return res * sign
            
        
            
        