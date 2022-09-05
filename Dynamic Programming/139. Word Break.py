
# O(N^3)
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        m = len(s)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        # iterate
        for end in range(1, m + 1):
            for start in range(end - 1, -1, -1):
                # check word
                if s[start:end] in wordDict:
                    dp[start][end] = 1
                # check combinations
                else:
                    if end > start + 1:
                        for k in range(start + 1, end):
                            if dp[start][k] * dp[k][end] > 0:
                                dp[start][end] = 1
                                break
        return dp[0][m] == 1
                
obj = Solution()
print(obj.wordBreak("leetcode", ["leet","code"]))

# O(N^3): search in a list is O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(i + 1, m + 1):
                if dp[i] == 1  and s[i:j] in wordDict:
                    dp[j] = 1
        return dp[m] == 1

# O(N^2): search in set is O(1), Python set is a hash table.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        wordSet = set(wordDict)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(m):
            for j in range(i + 1, m + 1):
                if dp[i] == 1  and s[i:j] in wordSet:
                    dp[j] = 1
        return dp[m] == 1