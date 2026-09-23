class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(grid, i, j)

        return result

    def dfs(self, grid, si, sj):
        m, n = len(grid), len(grid[0])
        stack = [(si, sj)]

        while stack:
            ci, cj = stack.pop()

            grid[ci][cj] = 0

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    stack.append((ni, nj))