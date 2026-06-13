class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            new_dp = dp.copy()

            for t in dp:
                if t + num == target:
                    return True

                new_dp.add(t + num)

            dp = new_dp

        return target in dp