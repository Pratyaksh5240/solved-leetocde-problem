class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if (nr, nc) in visited:
                    continue

                # Reverse the water flow:
                # move from ocean toward cells
                # that could flow into the ocean.
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # Pacific: top row + left column
        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, 0, pacific)

        # Atlantic: bottom row + right column
        for c in range(n):
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, n - 1, atlantic)

        result = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result