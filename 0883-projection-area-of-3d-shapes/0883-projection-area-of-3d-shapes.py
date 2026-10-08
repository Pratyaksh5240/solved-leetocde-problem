class Solution(object):
    def projectionArea(self, grid):
        n = len(grid)
        area = 0

        # Top view
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    area += 1

        # Front and side views
        for i in range(n):
            area += max(grid[i])  # row maximum

        for j in range(n):
            column_max = 0

            for i in range(n):
                column_max = max(column_max, grid[i][j])

            area += column_max

        return area