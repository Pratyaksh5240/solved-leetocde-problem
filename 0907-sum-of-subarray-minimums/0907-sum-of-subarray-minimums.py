class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7

        stack = []
        answer = 0

        for i in range(len(arr) + 1):

            current = arr[i] if i < len(arr) else 0

            while stack and (
                i == len(arr) or arr[stack[-1]] > current
            ):
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                countLeft = mid - left
                countRight = right - mid

                answer += (
                    arr[mid] *
                    countLeft *
                    countRight
                )

                answer %= MOD

            stack.append(i)

        return answer