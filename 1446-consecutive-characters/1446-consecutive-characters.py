class Solution(object):
    def maxPower(self, s):
        current = 1
        answer = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                current = 1

            answer = max(answer, current)

        return answer