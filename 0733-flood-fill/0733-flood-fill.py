class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]

        if original == color:
            return image

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= len(image) or
                c >= len(image[0]) or
                image[r][c] != original):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image