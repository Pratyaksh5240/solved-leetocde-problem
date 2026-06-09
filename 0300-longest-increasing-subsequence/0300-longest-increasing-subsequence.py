from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        lis = []

        for num in nums:
            pos = bisect_left(lis, num)

            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        return len(lis)