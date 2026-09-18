class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n, visited = len(board), len(board[0]), {}

        for i in range(m): # rows
            if not self._validate_row(board, i):
                return False

            for j in range(n): # columns
                if not self._validate_column(board, j):
                    return False

                if not self._validate_sub_box(board, i, j, visited):
                    return False

        return True

    def _validate_row(self, board, i):
        seen = set()

        for j in range(len(board[0])):
            value = board[i][j]

            if value is not "." and value in seen:
                return False

            seen.add(value)

        return True

    def _validate_column(self, board, j):
        seen = set()

        for i in range(len(board)):
            value = board[i][j]

            if value is not "." and value in seen:
                return False

            seen.add(value)

        return True

    def _validate_sub_box(self, board, i, j, visited):
        row, column = (i // 3) * 3, (j // 3) * 3

        if (row, column) in visited:
            return visited[(row, column)]

        seen = set()

        for di in range(3):
            for dj in range(3):
                value = board[row + di][column + dj]

                if value is not "." and value in seen:
                    return False

                seen.add(value)

        return True

