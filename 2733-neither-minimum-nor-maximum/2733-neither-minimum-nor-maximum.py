class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(set(nums)) < 3:
            return -1

        minimum = min(nums)
        maximum = max(nums)

        for num in nums:
            if num != minimum and num != maximum:
                return num

        return -1