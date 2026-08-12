class Solution(object):
    def longestStrChain(self, words):
        words.sort(key=len)

        dp = {}
        answer = 1

        for word in words:
            best = 1

            for i in range(len(word)):
                previous = word[:i] + word[i + 1:]

                if previous in dp:
                    best = max(best, dp[previous] + 1)

            dp[word] = best
            answer = max(answer, best)

        return answer