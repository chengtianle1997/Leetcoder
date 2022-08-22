
# with a dict, but without checking the whole dict, beat 25%+
class Solution:
    
    # move the start pointer forward, and return the new start pointer
    def shrink(self, s, start, end, cdict):
        while start < end:
            if s[start] in cdict.keys():
                if cdict[s[start]] < 0:
                    cdict[s[start]] += 1
                # if the char is an initial one, it cannot be shrinked any more
                else:
                    return start
            start += 1
        return start
                
        
    def minWindow(self, s: str, t: str) -> str:
        # create a dict to remember the substring, store the frequency of each char
        cdict = {}
        missing = 0
        for c in t:
            cdict[c] = cdict.get(c, 0) + 1
            missing += 1
        
        # init the indicators
        start = 0
        min_start = 0
        min_window = 1e5
        
        # iterate the end pointer
        for end in range(len(s)):
            # record the new element
            if s[end] in cdict.keys():
                cdict[s[end]] -= 1
                if cdict[s[end]] >= 0:
                    missing -= 1
            
            # if the window size is small, continue
            if end - start + 1 < len(t):
                continue   
                
            # check if the window is valid, shrink it to get a minimum size
            if missing == 0:
                start = self.shrink(s, start, end, cdict)
                size = end - start + 1
                if size < min_window:
                    min_window = size
                    min_start = start
        
        # handle the exception
        if min_window == 1e5:
            return ""
        
        # return the sub-string
        sub_s = s[min_start : min_start + min_window]
        
        return sub_s

# with a dict, beat 20%+
class Solution:
    
    def is_valid(self, cdict):
        for c in cdict.keys():
            if cdict[c] > 0:
                return False
        return True
    
    # move the start pointer forward, and return the new start pointer
    def shrink(self, s, start, end, cdict):
        while start < end:
            if s[start] in cdict.keys():
                if cdict[s[start]] < 0:
                    cdict[s[start]] += 1
                # if the char is an initial one, it cannot be shrinked any more
                else:
                    return start
            start += 1
        return start
                
        
        
    def minWindow(self, s: str, t: str) -> str:
        # create a dict to remember the substring, store the frequency of each char
        cdict = {}
        for c in t:
            cdict[c] = cdict.get(c, 0) + 1
        
        # init the indicators
        start = 0
        min_start = 0
        min_window = 1e5
        
        # iterate the end pointer
        for end in range(len(s)):
            # record the new element
            if s[end] in cdict.keys():
                cdict[s[end]] -= 1
            
            # if the window size is small, continue
            if end - start + 1 < len(t):
                continue
                
            # check if the window is valid, shrink it to get a minimum size
            if self.is_valid(cdict):
                start = self.shrink(s, start, end, cdict)
                size = end - start + 1
                if size < min_window:
                    min_window = size
                    min_start = start
        
        # handle the exception
        if min_window == 1e5:
            return ""
        
        # return the sub-string
        sub_s = s[min_start : min_start + min_window]
        
        return sub_s


# with a array with order index: beat 10%+
class Solution:
    
    def is_valid(self, cdict):
        for i in range(len(cdict)):
            if cdict[i] > 1:
                return False
        return True
    
    # move the start pointer forward, and return the new start pointer
    def shrink(self, s, start, end, cdict):
        while start < end: 
            if cdict[ord(s[start]) - ord('A')] < 1:
                cdict[ord(s[start]) - ord('A')] += 1
            # if the char is an initial one, it cannot be shrinked any more
            else:
                return start
            start += 1
        return start
                
        
    def minWindow(self, s: str, t: str) -> str:
        # create a array to remember the substring, store the frequency of each char
        # index: the order of char, val: 1: initial chars, >=1: chars rest
        cdict = [0] * (ord('z') - ord('A') + 1)
        for c in t:
            if cdict[ord(c) - ord('A')] == 0:
                cdict[ord(c) - ord('A')] = 1
            cdict[ord(c) - ord('A')] += 1
        
        # init the indicators
        start = 0
        min_start = 0
        min_window = 1e5
        
        # iterate the end pointer
        for end in range(len(s)):
            # record the new element
            cdict[ord(s[end]) - ord('A')] -= 1
            
            # if the window size is small, continue
            if end - start + 1 < len(t):
                continue
                
            # check if the window is valid, shrink it to get a minimum size
            if self.is_valid(cdict):
                start = self.shrink(s, start, end, cdict)
                size = end - start + 1
                if size < min_window:
                    min_window = size
                    min_start = start
        
        # handle the exception
        if min_window == 1e5:
            return ""
        
        # return the sub-string
        sub_s = s[min_start : min_start + min_window]
        
        return sub_s