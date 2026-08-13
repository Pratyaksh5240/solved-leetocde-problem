class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)

        if n == 0:
            return []

        pairs = [(nums[i], i) for i in range(n)]
        counts = [0] * n

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i = left
            j = mid
            right_count = 0

            while i < mid and j < right:

                if pairs[j][0] < pairs[i][0]:
                    temp.append(pairs[j])
                    right_count += 1
                    j += 1
                else:
                    counts[pairs[i][1]] += right_count
                    temp.append(pairs[i])
                    i += 1

            while i < mid:
                counts[pairs[i][1]] += right_count
                temp.append(pairs[i])
                i += 1

            while j < right:
                temp.append(pairs[j])
                j += 1

            for k in range(len(temp)):
                pairs[left + k] = temp[k]

        merge_sort(0, n)

        return counts