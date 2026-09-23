class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten, m, n = 0, collections.deque(), len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    rotten.append((i, j))

        time = 0
        while fresh > 0 and rotten:
            for _ in range(len(rotten)):
                ci, cj = rotten.popleft()
    
                for di, dj in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
                    ni, nj = ci + di, cj + dj
    
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        rotten.append((ni, nj))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1