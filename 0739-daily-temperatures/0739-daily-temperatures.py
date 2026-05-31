class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans