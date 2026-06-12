class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1] * n

        for _ in range(m - 1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]