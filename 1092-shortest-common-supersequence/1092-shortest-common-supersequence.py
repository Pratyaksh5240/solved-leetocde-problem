class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        i = 0
        j = 0
        answer = []

        while i < m and j < n:
            if str1[i] == str2[j]:
                answer.append(str1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] >= dp[i][j + 1]:
                answer.append(str1[i])
                i += 1

            else:
                answer.append(str2[j])
                j += 1

        while i < m:
            answer.append(str1[i])
            i += 1

        while j < n:
            answer.append(str2[j])
            j += 1

        return ''.join(answer)