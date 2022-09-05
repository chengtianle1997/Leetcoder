
# Beat 90%+
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start, maxlen = 0, 0
        for i in range(len(s)):
            if s[i] in used.keys() and used[s[i]] >= start:
                start = used[s[i]] + 1
            else:
                curlen = i - start + 1
                maxlen = max(maxlen, curlen)
            used[s[i]] = i
            
        return maxlen
                
            
        