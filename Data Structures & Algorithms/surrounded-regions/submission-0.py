class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n, border, visited = len(board), len(board[0]), set(), set()

        for i in range(m):
            if board[i][0] == "O":
                border.add((i, 0))

            if board[i][-1] == "O":
                border.add((i, n - 1))

        for j in range(n):
            if board[0][j] == "O":
                border.add((0, j))

            if board[-1][j] == "O":
                border.add((m - 1, j))

        while border:
            i, j = border.pop()
            visited.add((i, j))

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < m and 0 <= nj < n
                    and (ni, nj) not in visited
                    and board[ni][nj] == "O"
                ):
                    visited.add((ni, nj))
                    border.add((ni, nj))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"