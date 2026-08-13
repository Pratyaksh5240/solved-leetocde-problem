class NumArray(object):

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, value):
        while i <= self.n:
            self.bit[i] += value
            i += i & -i

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def _prefix_sum(self, i):
        total = 0

        while i > 0:
            total += self.bit[i]
            i -= i & -i

        return total

    def sumRange(self, left, right):
        return (
            self._prefix_sum(right + 1)
            - self._prefix_sum(left)
        )