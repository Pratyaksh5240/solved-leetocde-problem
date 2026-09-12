import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)

        # max heap using negative frequency
        heap = []

        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))

        result = []

        prevFreq = 0
        prevChar = ''

        while heap:
            freq, ch = heapq.heappop(heap)
            freq = -freq

            # We cannot place the same character twice
            if ch == prevChar:
                if not heap:
                    return ""

                freq2, ch2 = heapq.heappop(heap)
                freq2 = -freq2

                result.append(ch2)

                freq2 -= 1

                if freq2 > 0:
                    heapq.heappush(heap, (-freq2, ch2))

                heapq.heappush(heap, (-freq, ch))

                prevChar = ch2

            else:
                result.append(ch)

                freq -= 1

                if freq > 0:
                    heapq.heappush(heap, (-freq, ch))

                prevChar = ch

        return ''.join(result)