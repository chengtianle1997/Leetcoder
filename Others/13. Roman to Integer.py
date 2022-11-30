# A normal solution
class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            if s[i] == 'I':
                if (i + 1) < len(s) and s[i + 1] == 'V':
                    res += 4
                    i += 2
                elif (i + 1) < len(s) and s[i + 1] == 'X':
                    res += 9
                    i += 2
                else:
                    res += 1
                    i += 1
                continue
            if s[i] == 'X':
                if (i + 1) < len(s) and s[i + 1] == 'L':
                    res += 40
                    i += 2
                elif (i + 1) < len(s) and s[i + 1] == 'C':
                    res += 90
                    i += 2
                else:
                    res += 10
                    i += 1
                continue
            if s[i] == 'C':
                if (i + 1) < len(s) and s[i + 1] == 'D':
                    res += 400
                    i += 2
                elif (i + 1) < len(s) and s[i + 1] == 'M':
                    res += 900
                    i += 2
                else:
                    res += 100
                    i += 1
                continue
            if s[i] == 'V':
                res += 5
                i += 1
                continue
            if s[i] == 'L':
                res += 50
                i += 1
                continue
            if s[i] == 'D':
                res += 500
                i += 1
                continue
            if s[i] == 'M':
                res += 1000
                i += 1
                continue
        return res
            
# A smart idea
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # deal with the edge cases
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        res = 0
        for char in s:
            res += translations[char]
        return res
            