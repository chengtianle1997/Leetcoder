# Brute Force Solution, O(2^N)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # brute force solution
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # if there is a '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # we can use it, or not use it
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
                #       not use '*'            use '*'
            
            if match:
                return dfs(i + 1, j + 1)
            
            return False
        
        return dfs(0, 0)
                
# DP solution, caching, O(N^2)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        # DP solution, caching
        def dfs(i, j):
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # if there is a '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # we can use it, or not use it
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)
                
                