from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    max_area = max(
                        max_area, 
                        self.dfs(grid, i, j)
                    )

        return max_area

    def dfs(self, grid, i, j):
        area, queue, m, n = 1, deque([(i, j)]), len(grid), len(grid[0])
        grid[i][j] = 0

        while queue:
            ci, cj = queue.pop()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    queue.append((ni, nj))
                    grid[ni][nj] = 0
                    area += 1

        return area