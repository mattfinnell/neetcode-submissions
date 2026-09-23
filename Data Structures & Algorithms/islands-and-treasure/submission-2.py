from collections import deque
import math

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests, m, n = [], len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    chests.append((i, j, 0))

        queue = deque(chests)

        while queue:
            ci, cj, depth = queue.popleft()

            for di, dj in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 2147483647:
                    queue.append((ni, nj, depth + 1))
                    grid[ni][nj] = min(grid[ni][nj], depth + 1)
