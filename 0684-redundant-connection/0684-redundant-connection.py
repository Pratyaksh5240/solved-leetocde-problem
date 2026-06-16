class Solution(object):
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return False

            parent[pa] = pb
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]  