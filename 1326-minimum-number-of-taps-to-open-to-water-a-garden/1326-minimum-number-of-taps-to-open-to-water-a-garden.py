class Solution(object):
    def minTaps(self, n, ranges):
        maxReach = [0] * (n + 1)

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])

            maxReach[left] = max(
                maxReach[left],
                right
            )

        taps = 0
        currentEnd = 0
        farthest = 0

        for i in range(n):

            farthest = max(
                farthest,
                maxReach[i]
            )

            if i == currentEnd:

                if farthest <= currentEnd:
                    return -1

                taps += 1
                currentEnd = farthest

                if currentEnd >= n:
                    return taps

        return -1