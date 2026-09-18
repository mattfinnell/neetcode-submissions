class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter, m, n = 0, len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    counter += 1
        
        return counter
    
    def dfs(self, grid, i, j):
        stack = [(i, j)]

        while stack:
            i, j = stack.pop()

            grid[i][j] = "0"

            for ni, nj in self._get_neighbors(grid, i, j):
                if grid[ni][nj] == "1":
                    stack.append((ni, nj))

    def _get_neighbors(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                yield (ni, nj)

