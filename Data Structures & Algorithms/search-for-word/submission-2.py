class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self._dfs(board, word[1:], i, j, set()):
                    return True

        return False


    def _dfs(self, board, word, i, j, visited):
        m, n = len(board), len(board[0])

        if word == "":
            return True

        visited.add((i, j))
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if (
                0 <= ni < m and 0 <= nj < n and 
                board[ni][nj] == word[0] and 
                (ni, nj) not in visited and 
                self._dfs(board, word[1:], ni, nj, visited)
            ):
                return True

        visited.remove((i, j))

        return False