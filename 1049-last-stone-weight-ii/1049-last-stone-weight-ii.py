class Solution(object):
    def lastStoneWeightII(self, stones):
        total = sum(stones)

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        best = 0

        for j in range(target, -1, -1):
            if dp[j]:
                best = j
                break

        return total - 2 * best