class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            rob1 = rob2 = 0

            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )