
# Brute force solution, O(NM)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        p, q = 0, 0
        
        while p < len(haystack):
            # matching
            while p < len(haystack) and q < len(needle) and haystack[p] == needle[q]:
                p += 1
                q += 1
            
            # checking
            if q == len(needle):
                return p - len(needle)
            else:
                p -= q
                q = 0
            
            p += 1
            
        return -1
        

# Complicated KMP Solution, O(M + N)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        
        # The Longest Prefix Suffix
        preLPS, i = 0, 1
        lps = [0] * len(needle)
        
        while i < len(needle):
            if needle[i] == needle[preLPS]:
                lps[i] = preLPS + 1
                preLPS += 1
                i += 1
            elif preLPS == 0:
                lps[i] = 0
                i += 1
            else:
                preLPS = lps[preLPS - 1]
                
        i, j = 0, 0
        # i ptr for haystack, j ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                # matched
                return i - len(needle)
        
        return -1
        