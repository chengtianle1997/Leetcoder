
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # create a (m + 1) * (n + 1) DP matrix
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # iterate
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]

# Space Optimization: only 2 rows
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        # create a 2 * (n + 1) DP matrix
        dp = [[0] * (n + 1) for _ in range(2)]
        # iterate
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                else:
                    dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i - 1) % 2][j])
        return dp[m % 2][n]


#obj = Solution()
#print(obj.longestCommonSubsequence('abcba', 'abcbcba'))