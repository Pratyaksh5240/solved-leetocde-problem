class Solution(object):
    def rob(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2