class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            previous = 0

            for j in range(1, n + 1):
                temp = dp[j]

                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = previous + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                previous = temp

        return dp[n]