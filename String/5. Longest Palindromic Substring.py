
# Manacher Algorithm: Beat 95%+
class Solution:
    # return the expanded radius
    # input:
    # s: string, l: left index, r: right index
    def expand(self, s, l, r):
        ans = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            ans += 1
        return ans
    
    def longestPalindrome(self, s: str) -> str:
        
        # manacher algorithm
        
        # insert the #: aba -> #a#b#a#
        # to avoid considering odd and even conditions seperately
        t = "#"
        for c in s:
            t += c
            t += "#"
        s = t
            
        # initialize indicators
        p = [0] * len(s)
        center, mirror, max_right = 0, 0, 0
        # center = center index for the current palindromic 
        # mirror = 2 * center - i, which is the symetrical point of i about center
        # max_right = the rightest position we have explored
        # therefore, [2 * center - max_right, max_right] is symetrical about center
        
        # iterate the pointer i
        for i in range(len(s)):
            # if i is out of max_right, expanding needed
            if i >= max_right:
                # expand
                r = self.expand(s, i-1, i+1)
                p[i] = r
                center = i
                max_right = i + r
            # if i is in the range of max_right, reference existed
            else:
                mirror = 2 * center - i
                if p[mirror] < max_right - i:
                    p[i] = p[mirror]
                elif p[mirror] > max_right - i:
                    p[i] = max_right - i
                else:
                    # p[mirror] == max_right - i, expanding needed
                    r = self.expand(s, i - p[mirror] - 1, i + p[mirror] + 1)
                    center = i
                    max_right = i + r + p[mirror]
                    p[i] = r + p[mirror]
        
        # find the largest p
        l_i = 0
        l_p = 0
        for i in range(len(s)):
            if p[i] > l_p:
                l_p = p[i]
                l_i = i
        
        # output the substring
        sub_s = ""
        for i in range(l_i - l_p, l_i + l_p + 1, 1):
            if s[i] != "#":
                sub_s += s[i]
   
        return sub_s
                    
                    
        
        