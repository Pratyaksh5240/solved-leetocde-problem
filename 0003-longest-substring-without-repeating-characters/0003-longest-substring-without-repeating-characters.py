class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        answer = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right

            answer = max(answer, right - left + 1)

        return answer