from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))

        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m - 1, j))

        for i, j in list(pacific):
            self._bfs(heights, i, j, pacific)

        for i, j in list(atlantic):
            self._bfs(heights, i, j, atlantic)

        return [[i, j] for i, j in pacific & atlantic]

    def _bfs(self, heights, si, sj, ocean):
        queue, m, n = deque([(si, sj)]), len(heights), len(heights[0])

        while queue:
            i, j = queue.popleft()
            ocean.add((i, j))

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < m and 0 <= nj < n
                    and (ni, nj) not in ocean
                    and heights[ni][nj] >= heights[i][j]
                ):
                    queue.append((ni, nj))