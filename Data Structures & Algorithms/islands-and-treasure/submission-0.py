from collections import deque

INF = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue, m, n = deque(), len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, distance = queue.popleft()
            grid[i][j] = min(distance, grid[i][j])

            for ni, nj in self._get_neighbors(grid, i, j):
                if grid[ni][nj] == INF:
                    queue.append((ni, nj, distance + 1))

    def _get_neighbors(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                yield (ni, nj)