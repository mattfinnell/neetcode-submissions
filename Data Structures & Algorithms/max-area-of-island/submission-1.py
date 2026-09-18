class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        largest_island, visited, m, n = 0, set(), len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    largest_island = max(
                        largest_island, self._dfs(grid, (i, j), visited)
                    )

        return largest_island

    def _dfs(self, grid, start, visited) -> int:
        size, stack = 0, [start]
        visited.add(start)

        while stack:
            i, j = stack.pop()
            size += 1

            for ni, nj in self._get_neighbors(grid, i, j):
                if grid[ni][nj] == 1 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    stack.append((ni, nj))

        return size

    def _get_neighbors(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                yield ni, nj
