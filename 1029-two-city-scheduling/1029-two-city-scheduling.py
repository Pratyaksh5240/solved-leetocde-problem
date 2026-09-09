class Solution(object):
    def twoCitySchedCost(self, costs):
        # Sort by how much cheaper A is compared to B
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2

        answer = 0

        for i in range(n):
            answer += costs[i][0]

        for i in range(n, len(costs)):
            answer += costs[i][1]

        return answer