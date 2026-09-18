class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, m, n = 0, len(grid), len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j, visited))

        return max_area

    def dfs(self, grid, i, j, visited):
        depth, set_stack = 0, set([(i, j)])

        while set_stack:
            i, j = set_stack.pop()

            depth += 1
            visited.add((i, j))

            for ni, nj in self._get_neighbors(grid, i, j):
                if grid[ni][nj] == 1 and (ni, nj) not in visited:
                    set_stack.add((ni, nj))

        return depth

    def _get_neighbors(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                yield (ni, nj)
