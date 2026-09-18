class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit, queue, m, n = set(), deque(), len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_fruit.add((i, j))

                elif grid[i][j] == 2:
                    queue.append((i, j))


        time = 0
        while fresh_fruit:
            if not queue:
                return -1
            
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
    
                for ni, nj in self._get_neighbors(grid, i, j):
                    if grid[ni][nj] == 1 and (ni, nj) in fresh_fruit:
                        fresh_fruit.discard((ni, nj))
                        grid[ni][nj] = 2
                        queue.append((ni, nj))

        return time

    def _get_neighbors(self, grid, i, j):
        m, n = len(grid), len(grid[0])

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                yield (ni, nj)
        