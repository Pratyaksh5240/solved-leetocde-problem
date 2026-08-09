class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid, right)

            j = mid
            k = mid

            for i in range(left, mid):

                while j < right and prefix[j] - prefix[i] < lower:
                    j += 1

                while k < right and prefix[k] - prefix[i] <= upper:
                    k += 1

                count += k - j

            merged = []
            a = left
            b = mid

            while a < mid and b < right:
                if prefix[a] <= prefix[b]:
                    merged.append(prefix[a])
                    a += 1
                else:
                    merged.append(prefix[b])
                    b += 1

            while a < mid:
                merged.append(prefix[a])
                a += 1

            while b < right:
                merged.append(prefix[b])
                b += 1

            for i in range(len(merged)):
                prefix[left + i] = merged[i]

            return count

        return merge_sort(0, len(prefix))