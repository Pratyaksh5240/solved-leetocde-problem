class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)

        curMax = 1
        curMin = 1

        for n in nums:
            temp = curMax * n

            curMax = max(n, temp, curMin * n)
            curMin = min(n, temp, curMin * n)

            res = max(res, curMax)

        return res